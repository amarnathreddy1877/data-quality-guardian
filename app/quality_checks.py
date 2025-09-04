"""
app/quality_checks.py

This module contains functions to perform automated data quality checks on datasets.
It detects missing values, duplicates, data type issues, and outliers.

Designed for data analysts to quickly understand dataset issues before analysis.
"""

import pandas as pd

def run_quality_checks(df: pd.DataFrame) -> dict:
    """
    Run data quality checks on the given DataFrame.
    
    Parameters:
        df (pd.DataFrame): The dataset to check.
        
    Returns:
        dict: A report dictionary containing:
            - missing_values: columns with missing data and counts
            - duplicates: number of duplicate rows
            - data_types: column names with their data types
            - outliers: numeric columns with count of outliers (>3 std deviation)
    """
    
    report = {}

    # -----------------------------
    # 1️⃣ Missing Values Check
    # -----------------------------
    missing = df.isnull().sum()
    report['missing_values'] = missing[missing > 0].to_dict()

    # -----------------------------
    # 2️⃣ Duplicate Rows Check
    # -----------------------------
    report['duplicates'] = int(df.duplicated().sum())

    # -----------------------------
    # 3️⃣ Data Types Check
    # -----------------------------
    report['data_types'] = df.dtypes.astype(str).to_dict()

    # -----------------------------
    # 4️⃣ Outlier Detection (Numeric Columns)
    # Using basic rule: values beyond mean ± 3*std are considered outliers
    # -----------------------------
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    outliers = {}
    for col in numeric_cols:
        mean, std = df[col].mean(), df[col].std()
        outlier_count = ((df[col] > mean + 3*std) | (df[col] < mean - 3*std)).sum()
        outliers[col] = int(outlier_count)
    
    report['outliers'] = outliers

    return report
