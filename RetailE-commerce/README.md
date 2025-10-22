```markdown
````
# 🛍️ Online Retail Customer Behavior Analysis

## 📖 Overview
This project is an **interactive data analytics dashboard** built using **Streamlit** to analyze customer behavior from an online retail dataset.  
It provides **visual insights** about:
- Sales distribution across countries 🌍  
- Pricing and quantity patterns 📊  
- Customer sentiment from product descriptions 💬  

The dashboard allows users to **explore data visually** using Plotly charts and conduct **basic sentiment analysis** using TextBlob.


## 🚀 Features
✅ Interactive geographic visualization of transactions per country  
✅ Top 10 countries by total sales  
✅ Price and quantity distribution analysis  
✅ Relationship between price and quantity using heatmaps  
✅ Sentiment analysis on product descriptions (Positive / Negative / Neutral)  
✅ Key metrics in sidebar (Total Sales, Transactions, Average Order Value, Countries Served)

---

## 🧠 Tech Stack
| Category | Technologies |
|-----------|---------------|
| **Frontend & Dashboard** | Streamlit, Plotly |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Plotly, Seaborn, Matplotlib |
| **Text Processing** | TextBlob, Regex |
| **File Handling** | OpenPyXL, xlrd |

---

## 📂 Project Structure
```

📁 Online-Retail-Dashboard/
│
├── online_retail_II.xlsx         # Dataset file
├── app.py                        # Main Streamlit app
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/online-retail-dashboard.git
cd online-retail-dashboard
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🗺️ Dashboard Preview

Once you run the app, you’ll see the following tabs:

1. **Geographic Analysis** → Transaction distribution map & top countries by sales
2. **Price & Quantity Analysis** → Interactive histograms & heatmaps
3. **Sentiment Analysis** → Sentiment pie chart & average price by sentiment

Example:

```python
fig = px.choropleth(
    country_counts,
    locations='Country',
    locationmode='country names',
    color='Transactions',
    color_continuous_scale='viridis',
    title='Transactions by Country'
)
```

---

## 📊 Dataset Source

The dataset used in this project is the **Online Retail II Dataset** available on [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail+ii).
It contains transactional data from a UK-based online retail store between 2009–2011, including:

* Invoice and Stock details
* Product descriptions and prices
* Country information for each transaction

---

## 🧾 Key Metrics

| Metric                     | Description                          |
| -------------------------- | ------------------------------------ |
| 💰 **Total Sales**         | Sum of all product prices            |
| 🧾 **Total Transactions**  | Number of unique invoices            |
| 📦 **Average Order Value** | Total sales / number of transactions |
| 🌍 **Countries Served**    | Total number of countries in dataset |

---

## 💬 Sentiment Analysis

The sentiment analysis uses **TextBlob** to classify product descriptions:

* **Positive** → sentiment polarity > 0
* **Neutral** → sentiment polarity = 0
* **Negative** → sentiment polarity < 0

---

## 📊 Example Visualizations

**🗺️ Map:** Transactions by Country
**📈 Bar Chart:** Top 10 Countries by Sales
**💬 Pie Chart:** Sentiment Distribution
**🔥 Heatmap:** Price vs Quantity Relationship

---

## 📜 Requirements

All dependencies are listed in `requirements.txt`:

```txt
streamlit==1.50.0
pandas==2.3.3
numpy==2.2.0
matplotlib==3.9.2
seaborn==0.13.2
plotly==5.24.1
scikit-learn==1.5.2
scipy==1.14.1
joblib==1.4.2
requests==2.32.3
openpyxl==3.1.5
xlrd==2.0.1
textblob==0.18.0
```

---

## 📬 Contact

**Author:** Abdul Rahman Al-Shennawy
**Email:** [abdoalsenawework@gmail.com](mailto:abdoalsenawework@gmail.com)
**LinkedIn:** [linkedin.com/in/abdotech](https://www.linkedin.com/in/abdotech/)

```

