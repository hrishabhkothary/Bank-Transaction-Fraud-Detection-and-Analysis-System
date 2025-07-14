"""
utils.py

Reusable utility functions for the Bank Fraud Detection Project.
"""

import pandas as pd

def load_csv(filepath):
    """
    Load a CSV file into a Pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded data from {filepath} successfully.")
        return df
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None


def save_csv(df, filepath):
    """
    Save a Pandas DataFrame to a CSV file.
    """
    try:
        df.to_csv(filepath, index=False)
        print(f"Saved DataFrame to {filepath} successfully.")
    except Exception as e:
        print(f"Error saving to {filepath}: {e}")


def print_separator(title=""):
    """
    Print a separator for better notebook readability.
    """
    print("\n" + "="*50)
    if title:
        print(f" {title} ")
        print("="*50)
# """What does this do?
1. load_csv(): Safely loads any CSV — e.g., raw or processed transactions.

2. save_csv(): Saves your DataFrame safely — used after cleaning or feature engineering.

3. print_separator(): Helps keep your Jupyter notebook logs readable."""

