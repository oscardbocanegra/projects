import pandas as pd
import numpy as np

def analyze_data(df):
    """
    Performs a comprehensive analysis of the dataset and returns all relevant information in one call.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The input dataframe
    
    Returns:
    --------
    dict
        Dictionary containing all analysis results including:
        - Basic dataset information
        - Missing values information
        - Column-wise missing values
        - General information
    """
    # Basic dataset information
    dataset_info = {
        'Number of rows': len(df),
        'Number of columns': len(df.columns)
    }
    
    # Missing values information
    total_missing = df.isnull().sum().sum()
    total_cells = df.size
    percentage_missing = (total_missing / total_cells) * 100
    
    missing_values_info = {
        'Total missing values': total_missing,
        'Percentage of missing values': f"{percentage_missing:.2f}%"
    }
    
    # Column-wise missing values
    column_missing_info = pd.DataFrame({
        'Missing Values': df.isnull().sum(),
        'Percentage Missing': (df.isnull().sum() / len(df)) * 100
    })
    
    # General information
    general_info = {
        'Data Types': df.dtypes,
        'Memory Usage': f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
        'Number of Duplicates': df.duplicated().sum()
    }
    
    # Combine all information into a single dictionary
    analysis_results = {
        'Dataset Information': dataset_info,
        'Missing Values Summary': missing_values_info,
        'Column-wise Missing Values': column_missing_info,
        'General Information': general_info
    }
    
    return analysis_results 