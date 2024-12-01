# 1st Step: This code is used to test if your environment is set up properly and if the dataset loads correctly.

import pandas as pd

# Load the dataset
df = pd.read_csv('detailed_expenses.csv')

# Print the first few rows of the dataset to check
print(df.head())
