import pandas as pd
import numpy as np

# 0. Convert numeric columns from string

def convert_numeric(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


# 1. Handle Missing Values

def handle_missing_values(df):

    # Check for missing values

    missing_values = df.isnull().sum()
    print ('Missing values:\n', missing_values)

    # Replace missing values with appropriate values (e.g., mean, median, mode)

    df['coverage_estimate'].fillna(df['coverage_estimate'].mean(),
                                   inplace=True)
    df['population_sample_size'].fillna(df['population_sample_size'
            ].median(), inplace=True)


# 2. Handle Outliers

def handle_outliers(df):

    # Calculate Z-scores

    z_scores = (df['coverage_estimate'] - df['coverage_estimate'
                ].mean()) / df['coverage_estimate'].std()

    # Identify outliers based on Z-scores (e.g., Z-score > 3)

    outliers = df[z_scores > 3]
    print ('Outliers:\n', outliers)

    # Remove outliers

    df = df[z_scores <= 3]
    return df


# 3. Data Transformation

def transform_data(df):

    # Numerical data transformation: log transformation

    df['coverage_estimate_log'] = np.log(df['coverage_estimate'])

    # Create Derived Variables

    df['coverage_rate'] = df['coverage_estimate'] \
        / df['population_sample_size']
    return df


# 4. Aggregate Data

def aggregate_data(df):
    df_aggregated = df.groupby(['year_season', 'geography_type'
                               ]).agg({'coverage_estimate': 'mean'})
    return df_aggregated
