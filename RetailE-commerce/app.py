import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from textblob import TextBlob
import re

# Set page config
st.set_page_config(
    page_title="Online Retail Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# Title
st.title("🛍️ Online Retail Customer Behavior Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel('online_retail_II.xlsx')
    # Data cleaning
    df.drop(columns=['Customer ID', 'StockCode'], inplace=True)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    # Clean price and quantity
    df = df[df['Price'] > 0]
    df = df[df['Price'] < df['Price'].quantile(0.99)]
    df = df[df['Quantity'] > 0]
    df = df[df['Quantity'] < df['Quantity'].quantile(0.99)]
    
    # Replace EIRE with Ireland for mapping
    df['Country'] = df['Country'].replace({'EIRE': 'Ireland'})
    
    return df

# Load the data
df = load_data()

# Create tabs
tab1, tab2, tab3 = st.tabs(["Geographic Analysis", "Price & Quantity Analysis", "Sentiment Analysis"])

with tab1:
    st.header("Geographic Analysis")
    
    # Country transactions map
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Transactions']
    
    fig_map = px.choropleth(
        country_counts,
        locations='Country',
        locationmode='country names',
        color='Transactions',
        color_continuous_scale='viridis',
        title='Transactions by Country',
        labels={'Transactions': 'Number of Transactions'},
        hover_name='Country'
    )
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Top countries by sales
    country_sales = df.groupby('Country').agg({
        'Price': 'sum',
        'Invoice': 'count'
    }).reset_index()
    country_sales.columns = ['Country', 'Total Sales', 'Number of Transactions']
    country_sales = country_sales.sort_values('Total Sales', ascending=False).head(10)
    
    fig_sales = px.bar(
        country_sales,
        x='Country',
        y='Total Sales',
        title='Top 10 Countries by Total Sales',
        color='Total Sales',
        color_continuous_scale='viridis'
    )
    st.plotly_chart(fig_sales, use_container_width=True)

with tab2:
    st.header("Price & Quantity Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Price distribution
        fig_price = px.histogram(
            df,
            x='Price',
            nbins=50,
            title='Price Distribution',
            labels={'Price': 'Price (£)'},
            color_discrete_sequence=['skyblue']
        )
        st.plotly_chart(fig_price, use_container_width=True)
    
    with col2:
        # Quantity distribution
        fig_quantity = px.histogram(
            df,
            x='Quantity',
            nbins=50,
            title='Quantity Distribution',
            color_discrete_sequence=['lightgreen']
        )
        st.plotly_chart(fig_quantity, use_container_width=True)
    
    # Price vs Quantity hexbin plot
    fig_hex = px.density_heatmap(
        df,
        x='Price',
        y='Quantity',
        title='Price vs Quantity Relationship',
        nbinsx=40,
        nbinsy=40,
        color_continuous_scale='viridis'
    )
    st.plotly_chart(fig_hex, use_container_width=True)

with tab3:
    st.header("Sentiment Analysis")
    
    # Function to clean text and get sentiment
    @st.cache_data
    def process_sentiment(df):
        def clean_text(text):
            if pd.isnull(text):
                return ""
            text = str(text).lower()
            text = re.sub(r'[^a-z\s]', '', text)
            text = re.sub(r'\s+', ' ', text)
            return text.strip()
        
        def get_sentiment(text):
            if pd.isnull(text):
                return None
            blob = TextBlob(text)
            return blob.sentiment.polarity
        
        df['clean_description'] = df['Description'].apply(clean_text)
        df['sentiment_score'] = df['clean_description'].apply(get_sentiment)
        df['sentiment_label'] = df['sentiment_score'].apply(
            lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
        )
        return df
    
    # Process sentiment
    df_sentiment = process_sentiment(df)
    
    # Sentiment distribution
    sentiment_counts = df_sentiment['sentiment_label'].value_counts()
    
    fig_sentiment = px.pie(
        values=sentiment_counts.values,
        names=sentiment_counts.index,
        title='Product Description Sentiment Distribution',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_sentiment, use_container_width=True)
    
    # Average price by sentiment
    avg_price_sentiment = df_sentiment.groupby('sentiment_label')['Price'].mean().reset_index()
    fig_price_sentiment = px.bar(
        avg_price_sentiment,
        x='sentiment_label',
        y='Price',
        title='Average Price by Sentiment',
        color='sentiment_label',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_price_sentiment, use_container_width=True)

# Sidebar with key metrics
st.sidebar.header("Key Metrics")
total_sales = df['Price'].sum()
total_transactions = len(df['Invoice'].unique())
average_order_value = total_sales / total_transactions
total_countries = df['Country'].nunique()

st.sidebar.metric("Total Sales", f"£{total_sales:,.2f}")
st.sidebar.metric("Total Transactions", f"{total_transactions:,}")
st.sidebar.metric("Average Order Value", f"£{average_order_value:.2f}")
st.sidebar.metric("Countries Served", total_countries)
