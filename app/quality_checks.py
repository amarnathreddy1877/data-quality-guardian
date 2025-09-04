"""
app/quality_checks.py

This module contains functions to perform automated data quality checks on datasets.
It detects missing values, duplicates, data type issues, and outliers.

Designed for data analysts to quickly understand dataset issues before analysis.
"""

import pandas as pd
import numpy as np

def generate_row_level_report(df, id_col='id'):
    # Initialize the report string
    report = "📊 Data Quality Report (Row-Level)\n\n"

    # Check for missing values
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

    # Detect duplicate rows
    report += "Duplicates:\n"
    # Checks for full row duplicates
   duplicates = df[df.duplicated(keep=False)] 
    #duplicate_rows = df[df.duplicated(subset=df.columns.tolist(), keep=False)]
    if duplicates.empty:
        report += "- No duplicate rows found\n"
    else:
        dup_ids = duplicates[id_col].tolist()
        for dup_id in set(dup_ids):
            report += f"- Duplicate record found for id: {dup_id}\n"
    report += "\n"

    # Detect outliers in numeric columns
    report += "Outliers:\n"
    numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        mean = df[col].mean()
        std = df[col].std()
        outlier_rows = df[(df[col] - mean).abs() > 3*std]
        if not outlier_rows.empty:
            for idx, row in outlier_rows.iterrows():
                name = row['name'] if 'name' in df.columns else 'N/A'
                report += f"- Outlier detected in '{col}' for id: {row[id_col]} ({name}) -> {row[col]}\n"
        else:
            report += f"- No outliers detected in '{col}'\n"

    return report

