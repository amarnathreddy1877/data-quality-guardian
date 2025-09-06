# 📊 Data Quality Guardian

**Data Quality Guardian** is an interactive **row-level data quality analysis tool** built with **Python & Streamlit**.  
It enables data analysts and teams to **detect missing values, duplicate records, and outliers** in CSV datasets with **actionable, row-level insights**.  

This project demonstrates practical **data cleaning, preprocessing, and interactive dashboard development skills**, making it a strong portfolio project for recruiters and hiring managers.  

---

## 🌟 Features

- ✅ **Missing Values Detection** – Identify missing values per row and column  
- ✅ **Duplicate Record Detection** – Detect duplicates across all columns  
- ✅ **Adaptive Outlier Detection**  
  - IQR method for **small datasets (< 50 rows)**  
  - Z-score method for **large datasets (≥ 50 rows)**  
- ✅ **Row-Level Report** – Clear, human-readable report with IDs & values  
- ✅ **Interactive Exploration** – Filter issues by category (Missing, Duplicates, Outliers)  
- ✅ **Download Options** – Export full report (`.txt`) or filtered rows (`.csv`)  
- 🖥️ **Built with Streamlit** – Easy to run locally or deploy on the web  

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
# 1. Clone the repository
# Clone your GitHub repository
git clone <your_repo_url>

# Move into the project directory
cd data-quality-guardian


# 2. Setup Python Environment
Option A: Using system Python
# Check Python version (must be 3.9+)
python --version

# Or on some systems
python3 --version

# Optional: Using virtual environment (recommended)
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

#✅ Using a virtual environment keeps dependencies isolated and avoids conflicts.


#3. Install Dependencies
# Install all required Python packages
pip install -r requirements.txt


#4. Run the Streamlit App
# Run the interactive app
streamlit run app/main.py

#5.Deactivate virtual environment
deactivate


