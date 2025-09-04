"""
app/main.py

Streamlit web application for the Data Quality Guardian.
Allows users to upload CSV datasets, run automated quality checks,
and get AI-generated explanations for issues.
"""
import streamlit as st
import pandas as pd
from io import StringIO
from quality_checks import generate_row_level_report

st.title("Data Quality Guardian - Interactive Row-Level Report")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Load CSV into DataFrame
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Generate row-level report
    report = generate_row_level_report(df, id_col='id')
    st.subheader("Data Quality Report (Plain Text)")
    st.text(report)

    # Download full report as text file
    st.download_button(
        label="Download Full Report",
        data=report,
        file_name="data_quality_report.txt",
        mime="text/plain"
    )

    # Interactive filtering for specific issues
    st.subheader("View Specific Issues")
    issue_type = st.selectbox("Select Issue Type", ["Missing Values", "Duplicates", "Outliers"])

    filtered_rows = pd.DataFrame()

    if issue_type == "Missing Values":
        filtered_rows = df[df.isnull().any(axis=1)]
        st.write("Rows with missing values:" if not filtered_rows.empty else "No missing values found")
        if not filtered_rows.empty:
            st.dataframe(filtered_rows)

    elif issue_type == "Duplicates":
        filtered_rows = df[df.duplicated(subset=df.columns.tolist(), keep=False)]
        st.write("Duplicate rows:" if not filtered_rows.empty else "No duplicate rows found")
        if not filtered_rows.empty:
            st.dataframe(filtered_rows)

    elif issue_type == "Outliers":
        numeric_cols = df.select_dtypes(include='number').columns
        outlier_rows = pd.DataFrame()
        for col in numeric_cols:
            col_series = pd.to_numeric(df[col], errors='coerce').dropna()
            if len(col_series) < 50:
                Q1 = col_series.quantile(0.25)
                Q3 = col_series.quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            else:
                mean = col_series.mean()
                std = col_series.std()
                outliers = df[(df[col] - mean).abs() > 3 * std]
            outlier_rows = pd.concat([outlier_rows, outliers])
        filtered_rows = outlier_rows.drop_duplicates()
        st.write("Rows with outliers:" if not filtered_rows.empty else "No outliers detected")
        if not filtered_rows.empty:
            st.dataframe(filtered_rows)

    # Download filtered rows as CSV if any exist
    if not filtered_rows.empty:
        csv_buffer = StringIO()
        filtered_rows.to_csv(csv_buffer, index=False)
        st.download_button(
            label=f"Download {issue_type} Rows as CSV",
            data=csv_buffer.getvalue(),
            file_name=f"{issue_type.replace(' ', '_').lower()}_rows.csv",
            mime="text/csv"
        )

