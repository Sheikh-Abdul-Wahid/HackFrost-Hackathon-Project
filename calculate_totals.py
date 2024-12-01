# 2nd Step: Python code for calculating monthly totals

import pandas as pd

# Load the dataset
data = pd.read_csv('detailed_expenses.csv')

# Group by month and sum the total prices
monthly_totals = data.groupby('Month')['Total Price($)'].sum().reset_index()

# Rename columns for clarity
monthly_totals.columns = ['Month', 'Total Expense($)']

# Define the correct month order
month_order = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Sort the data by the defined month order
monthly_totals['Month'] = pd.Categorical(monthly_totals['Month'], categories=month_order, ordered=True)
monthly_totals = monthly_totals.sort_values('Month')

# Display the monthly totals
print("Monthly Total Expenses:")
print(monthly_totals)

# Save the processed data
monthly_totals.to_csv('monthly_total_expenses.csv', index=False)
