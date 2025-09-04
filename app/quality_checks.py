"""
app/quality_checks.py

This module contains functions to perform automated data quality checks on datasets.
It detects missing values, duplicates, data type issues, and outliers.

Designed for data analysts to quickly understand dataset issues before analysis.
"""
import pandas as pd
import numpy as np

def generate_row_level_report(df, id_col='id'):
    """
    Generate a row-level data quality report for the given DataFrame.
    Checks for missing values, duplicates, and outliers in numeric columns.
    """

    report = "📊 Data Quality Report (Row-Level)\n\n"

    # ----- Missing Values -----
    report += "Missing Values:\n"
    missing = df.isnull()
    if missing.sum().sum() == 0:
        report += "- No missing values found\n"
    else:
        for col in df.columns:
            if missing[col].sum() > 0:
                missing_rows = df[df[col].isnull()][id_col].tolist()
                names = df[df[col].isnull()]['name'].tolist() if 'name' in df.columns else ['N/A']*len(missing_rows)
                for i, row_id in enumerate(missing_rows):
                    report += f"- '{col}' missing for id: {row_id} ({names[i]})\n"
    report += "\n"

    # ----- Duplicates -----
    report += "Duplicates:\n"
    duplicates = df[df.duplicated(subset=df.columns.tolist(), keep=False)]
    if duplicates.empty:
        report += "- No duplicate rows found\n"
    else:
        dup_ids = duplicates[id_col].tolist()
        for dup_id in set(dup_ids):
            report += f"- Duplicate record found for id: {dup_id}\n"
    report += "\n"

    # ----- Outliers -----
    report += "Outliers:\n"
    numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        col_series = pd.to_numeric(df[col], errors='coerce').dropna()
        
        if len(col_series) < 50:
            # Small dataset → use IQR
            Q1 = col_series.quantile(0.25)
            Q3 = col_series.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outlier_rows = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        else:
            # Large dataset → use z-score
            mean = col_series.mean()
            std = col_series.std()
            outlier_rows = df[(df[col] - mean).abs() > 3 * std]
        
        if not outlier_rows.empty:
            for idx, row in outlier_rows.iterrows():
                name = row['name'] if 'name' in df.columns else 'N/A'
                report += f"- Outlier detected in '{col}' for id: {row[id_col]} ({name}) -> {row[col]}\n"
        else:
            report += f"- No outliers detected in '{col}'\n"

    return report
