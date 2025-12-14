# Pandas Examples Script
# Author: RSK World
# Website: https://rskworld.in
# Email: help@rskworld.in
# Phone: +91 93305 39277
# Description: Example Python scripts demonstrating various Pandas operations

import pandas as pd
import numpy as np
import os

# Change to script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(os.path.dirname(script_dir), 'data')

print("=" * 60)
print("Pandas Data Manipulation Examples")
print("Author: RSK World | Website: https://rskworld.in")
print("=" * 60)


def example_read_csv():
    """Example: Reading CSV files"""
    print("\n1. Reading CSV File")
    print("-" * 60)
    csv_path = os.path.join(data_dir, 'sample_data.csv')
    df = pd.read_csv(csv_path)
    print(df)
    return df


def example_basic_operations(df):
    """Example: Basic DataFrame operations"""
    print("\n2. Basic Operations")
    print("-" * 60)
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"\nFirst 3 rows:")
    print(df.head(3))
    print(f"\nDataFrame Info:")
    print(df.info())


def example_filtering(df):
    """Example: Filtering data"""
    print("\n3. Filtering")
    print("-" * 60)
    filtered = df[df['Salary'] > 60000]
    print("Employees with Salary > 60000:")
    print(filtered[['Name', 'Department', 'Salary']])


def example_groupby(df):
    """Example: GroupBy operations"""
    print("\n4. GroupBy Operations")
    print("-" * 60)
    dept_stats = df.groupby('Department')['Salary'].agg(['mean', 'min', 'max', 'count'])
    print("Department Salary Statistics:")
    print(dept_stats)


def example_merging():
    """Example: Merging DataFrames"""
    print("\n5. Merging DataFrames")
    print("-" * 60)
    df1 = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David']
    })
    
    df2 = pd.DataFrame({
        'ID': [1, 2, 3, 5],
        'Salary': [50000, 60000, 70000, 55000]
    })
    
    merged = pd.merge(df1, df2, on='ID', how='inner')
    print("Merged DataFrame:")
    print(merged)


def example_data_cleaning():
    """Example: Data cleaning"""
    print("\n6. Data Cleaning")
    print("-" * 60)
    # Create DataFrame with missing values
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [25, 30, None, 28],
        'Salary': [50000, None, 70000, 55000]
    })
    
    print("Original DataFrame:")
    print(df)
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Fill missing values
    df_cleaned = df.copy()
    df_cleaned['Age'].fillna(df_cleaned['Age'].mean(), inplace=True)
    df_cleaned['Salary'].fillna(df_cleaned['Salary'].median(), inplace=True)
    df_cleaned['Name'].fillna('Unknown', inplace=True)
    
    print("\nAfter cleaning:")
    print(df_cleaned)


def example_transformations(df):
    """Example: Data transformations"""
    print("\n7. Data Transformations")
    print("-" * 60)
    df_transformed = df.copy()
    
    # Add new column
    df_transformed['Bonus'] = df_transformed['Salary'] * 0.1
    df_transformed['Total'] = df_transformed['Salary'] + df_transformed['Bonus']
    
    # Categorize salary
    df_transformed['Salary_Category'] = df_transformed['Salary'].apply(
        lambda x: 'High' if x > 65000 else 'Medium' if x > 55000 else 'Low'
    )
    
    print("Transformed DataFrame:")
    print(df_transformed[['Name', 'Salary', 'Bonus', 'Total', 'Salary_Category']])


if __name__ == "__main__":
    # Run examples
    df = example_read_csv()
    example_basic_operations(df)
    example_filtering(df)
    example_groupby(df)
    example_merging()
    example_data_cleaning()
    example_transformations(df)
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)

