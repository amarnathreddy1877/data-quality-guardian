# 🛡️ Data Quality Guardian  

An **AI-powered data quality assistant** that automatically scans datasets, detects issues (missing values, duplicates, outliers, schema drift), and provides **plain-English explanations with suggested fixes**.  

🚀 Built for Data Analysts who want to **save time cleaning data** and **communicate data quality clearly to stakeholders**.  

---

## ✨ Features
- 🔍 Detects:
  - Missing values  
  - Duplicate rows  
  - Data type mismatches  
  - Outliers (statistical check: ±3 standard deviations)  
- 🤖 AI-generated explanations of issues  
- 🛠️ Suggested code fixes (Pandas & SQL)  
- 🖥️ Streamlit web app interface  
- 📊 Example dataset included  

---

## 📂 Project Structure
data-quality-guardian/
│── app/
│ ├── quality_checks.py # Core data quality checks
│ ├── ai_explainer.py # AI explanations + fixes
│ └── main.py # Streamlit app
│── data/
│ └── sample_data.csv # Example dataset
│── requirements.txt # Dependencies
│── README.md # Project documentation
