# Libreria EDA

A Python library for Exploratory Data Analysis (EDA) that provides comprehensive data analysis in a single function call.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
import pandas as pd
from libreria_eda import analyze_data

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Get comprehensive analysis of your dataset
analysis_results = analyze_data(df)

# Access different parts of the analysis
print("Dataset Information:", analysis_results['Dataset Information'])
print("\nMissing Values Summary:", analysis_results['Missing Values Summary'])
print("\nColumn-wise Missing Values:")
print(analysis_results['Column-wise Missing Values'])
print("\nGeneral Information:", analysis_results['General Information'])
```

## Function

`analyze_data(df)`
- Returns a comprehensive analysis of the dataset including:
  - Basic dataset information (number of rows and columns)
  - Missing values summary (total and percentage)
  - Column-wise missing values information
  - General information (data types, memory usage, duplicates)

## Requirements

- Python 3.6+
- pandas
- numpy 