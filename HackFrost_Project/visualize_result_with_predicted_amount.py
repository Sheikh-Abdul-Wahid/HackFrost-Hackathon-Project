# 3rd Step: Use a Machine Learning Model (Linear Regression) to predict next month's expenses and generate plot for better understanding.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the processed data
processed_data = pd.read_csv('monthly_total_expenses.csv')

# Prepare features (month indices) and target (total expenses)
X = np.arange(len(processed_data)).reshape(-1, 1)  # Months as numeric indices
y = processed_data['Total Expense($)'].values  # Total expenses

# Extract month names for x-axis labels
month_names = processed_data['Month'].tolist()

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict next month's expense
next_month_index = np.array([[len(X)]])  # Next month's index
predicted_expense = model.predict(next_month_index)

# Save the prediction result
prediction = pd.DataFrame({'Month': ['Next Month'], 'Predicted Expense($)': [predicted_expense[0]]})
prediction.to_csv('predicted_expense.csv', index=False)

# Display prediction
print(f"\nPredicted Expense for Next Month: ${predicted_expense[0]:.2f}")

# Visualization
plt.plot(X, y, marker='o', label='Historical Expenses')  # Historical data
plt.scatter(len(X), predicted_expense, color='red', label='Predicted Expense')  # Prediction

# Customize x-axis
plt.xticks(ticks=np.arange(len(month_names)), labels=month_names, rotation=45)

# Add labels, legend, and title
plt.title("Monthly Expenses Prediction in $")
plt.xlabel("Month")
plt.ylabel("Total Expense ($)")
plt.legend()
plt.grid()
plt.tight_layout()  # Adjust layout for better visibility

# Show plot
plt.show()
