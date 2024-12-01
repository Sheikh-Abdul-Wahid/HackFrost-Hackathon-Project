# HackFrost Hackathon Project: Machine Learning Workflow for Expense Prediction
This project was developed as part of the HackFrost Hackathon. It uses Python and Kestra workflows to analyze monthly expenses, predict future expenses, and visualize the results. The workflow integrates Python scripts with Kestra to automate data processing, prediction, and visualization.

## 📂 Project Structure:

Here’s an overview of the files in this repository:

- `detailed_expenses.csv`: The dataset containing monthly expense details.
- `kestra_hackfrost_hackathon_project.yaml`: The Kestra workflow configuration file that orchestrates the project tasks.
- `test_setup.py`: Python script to fetch and verify the dataset.
- `calculate_totals.py`: Python script to calculate monthly expense totals.
- `visualize_results.py`: Python script to predict next month’s expenses and generate visualizations.

## 🚀 Features:

1. **Automated Workflow with Kestra**:  
The project uses `Kestra` workflows to manage tasks such as fetching data, processing it, and generating predictions.

2. **Expense Analysis**:  
Monthly expenses are analyzed, grouped, and sorted for better understanding.

3. **Expense Prediction**:  
`Linear Regression` is used to predict the expense for the next month based on historical data.

4. **Visualization**:  
A line plot with predictions highlights historical expenses and future projections.

## 🛠️ Setup and Execution:

### Prerequisites
- Docker: Ensure Docker is installed on your system.
- Kestra: This project uses Kestra workflows, and the setup is managed through Docker Compose.

### Steps to Run
1. **Clone the repository**:
```bash
git clone https://github.com/Sheikh-Abdul-Wahid/HackFrost-Hackathon-Project.git
cd HackFrost-Hackathon-Project

