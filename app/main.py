"""
app/main.py

Streamlit web application for the Data Quality Guardian.
Allows users to upload CSV datasets, run automated quality checks,
and get AI-generated explanations for issues.
"""

import streamlit as st
import pandas as pd
from app.quality_checks import run_quality_checks
from app.ai_explainer import explain_issues

# -----------------------------
# 1️⃣ Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Data Quality Guardian",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# 2️⃣ App Title & Description
# -----------------------------
st.title("🛡️ Data Quality Guardian")
st.markdown("""
Upload a CSV dataset to automatically check for:
- Missing values
- Duplicate rows
- Data type issues
- Outliers

Click the **Generate AI Explanation** button to get plain-English insights and suggested fixes.
""")

# -----------------------------
# 3️⃣ File Uploader
# -----------------------------
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    # Load CSV
    df = pd.read_csv(uploaded_file)
    st.success("✅ Data Loaded Successfully!")
    
    # Show first 5 rows
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    # -----------------------------
    # 4️⃣ Run Data Quality Checks
    # -----------------------------
    report = run_quality_checks(df)
    st.subheader("📊 Data Quality Report")
    st.json(report)

    # -----------------------------
    # 5️⃣ Generate AI Explanations
    # -----------------------------
    if st.button("🧠 Generate AI Explanation"):
        with st.spinner("Analyzing dataset with AI..."):
            explanation = explain_issues(report)
        st.subheader("📝 AI Insights & Suggested Fixes")
        st.markdown(explanation)

else:
    st.info("Please upload a CSV file to get started.")
