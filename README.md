# 📊 Data Quality Guardian

**Data Quality Guardian** is an interactive data quality tool designed for **analysts and data engineers**. It identifies **missing values, duplicate records, and outliers** in CSV datasets and generates **row-level actionable reports**. Built with **Python**, **Pandas**, and **Streamlit**, this project demonstrates modern data analysis and automation skills.

---

## 🚀 Key Features

- **Row-Level Insights:** Pinpoints exactly which rows have missing data, duplicates, or outliers.
- **Interactive Exploration:** Filter by issue type (Missing Values, Duplicates, Outliers) and inspect affected rows directly in the app.
- **Exportable Reports:** Download full reports as `.txt` or filtered rows as `.csv` for further analysis.
- **Recruiter-Friendly Presentation:** Plain-text reports with clear, actionable messages for decision-makers.
- **Reusable for Any CSV Dataset:** Works with any CSV that has a unique `id` column.

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Pandas** – Data manipulation and analysis  
- **NumPy** – Numeric operations and outlier detection  
- **Streamlit** – Interactive web interface  
- **IO** – CSV and text file export  

---

## 🎯 Demo Screenshots

**1️⃣ Dataset Preview**  

![Dataset Preview](https://via.placeholder.com/600x150.png?text=Dataset+Preview)

**2️⃣ Row-Level Data Quality Report**  

![Data Quality Report](https://via.placeholder.com/600x200.png?text=Row-Level+Report)

**3️⃣ Filtered Issue View & Download Option**  

![Filtered Rows](https://via.placeholder.com/600x200.png?text=Filtered+Rows+Download)

*(Replace placeholders with actual screenshots from your app)*

---

## 💡 How It Works

1. Upload a CSV file containing your dataset.  
2. The app automatically analyzes the data and generates a **row-level report**:  
   - Which columns have missing values  
   - Duplicate rows detected  
   - Outliers in numeric columns  
3. Explore interactive tables for each issue type.  
4. Download the **full report** or **filtered rows** as `.csv` for downstream analysis.

---

## 🗂️ Sample Data

The `data/` folder includes **3 sample CSV files** demonstrating different issues:

| File Name | Description |
|-----------|-------------|
| `sample_data1.csv` | Contains missing values, duplicates, and outliers |
| `sample_data2.csv` | Includes missing salary values and duplicates |
| `sample_data3.csv` | Demonstrates numeric outliers for products |

---


## 🚀 Run the Data Quality Guardian App

Follow these simple steps to run the app locally:

Tip: After running, your browser should open automatically.
If it doesn’t, copy the Local URL from the terminal (usually http://localhost:8501) and open it manually.
Use sample CSV files from the data/ folder to test the app quickly.


```bash
# 1️⃣ Clone the repository
git clone https://github.com/amarnathreddy1877/data-quality-guardian.git
cd data-quality-guardian

# 2️⃣ Install required Python packages
pip install -r requirements.txt

# 3️⃣ Launch the interactive Streamlit app
streamlit run app/main.py



