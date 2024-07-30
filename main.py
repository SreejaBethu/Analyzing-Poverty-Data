import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import pearsonr
import os

# Set up the visual style
sns.set(style="whitegrid")

# Full path to the file
file_path = "C:/Users/Sreeja/PycharmProjects/Analyzing Poverty Data/PovStatsCountry.csv"  # Update with the actual path if needed

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        # Load the data
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")

        # Display the first few rows of the dataset
        print(data.head())

        # Print all column names before renaming
        print("Columns in the dataset before renaming:\n", data.columns)

        # Assuming these are the correct columns for income and poverty rate
        poverty_rate_column = 'Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)'
        income_column = 'GNI per capita, Atlas method (current US$)'

        # Renaming columns for easier access (if necessary)
        data.rename(columns={
            'Country Name': 'Country',
            'Region': 'Region',
            poverty_rate_column: 'Poverty_Rate',
            income_column: 'Income'
        }, inplace=True)

        # Verify the renamed columns
        print("Renamed Columns:\n", data.columns)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        data = None

    if data is not None:
        # Check if the expected columns exist after renaming
        if 'Income' not in data.columns or 'Poverty_Rate' not in data.columns or 'Region' not in data.columns:
            print("One or more columns ('Income', 'Poverty_Rate', 'Region') are missing after renaming.")
        else:
            # Drop rows with significant missing values in key columns
            data_cleaned = data.dropna(subset=['Income', 'Poverty_Rate', 'Region'])

            # Display the cleaned data
            print(data_cleaned.head())

            # Summary statistics
            summary = data_cleaned.describe()
            print(summary)

            # Distribution of income levels
            plt.figure(figsize=(10, 6))
            sns.histplot(data_cleaned['Income'], kde=True)
            plt.title('Income Distribution')
            plt.xlabel('Income')
            plt.ylabel('Frequency')
            plt.show()

            # Poverty rate by region
            plt.figure(figsize=(12, 8))
            sns.boxplot(x='Region', y='Poverty_Rate', data=data_cleaned)
            plt.title('Poverty Rate by Region')
            plt.xlabel('Region')
            plt.ylabel('Poverty Rate')
            plt.xticks(rotation=45)
            plt.show()

            # Correlation matrix
            plt.figure(figsize=(10, 8))
            corr_matrix = data_cleaned.corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
            plt.title('Correlation Matrix')
            plt.show()

            # Scatter plot of Poverty Rate vs. Income
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x='Income', y='Poverty_Rate', data=data_cleaned, hue='Region')
            plt.title('Poverty Rate vs. Income')
            plt.xlabel('Income')
            plt.ylabel('Poverty Rate')
            plt.show()

            # Line plot of Poverty Rate over Years for different Regions
            plt.figure(figsize=(14, 8))
            sns.lineplot(x='Year', y='Poverty_Rate', hue='Region', data=data_cleaned, marker='o')
            plt.title('Poverty Rate Over Years by Region')
            plt.xlabel('Year')
            plt.ylabel('Poverty Rate')
            plt.legend(title='Region')
            plt.show()

            # Correlation between Income and Poverty Rate
            correlation, p_value = pearsonr(data_cleaned['Income'], data_cleaned['Poverty_Rate'])
            print(f'Correlation: {correlation}, P-value: {p_value}')

            # Linear Regression Analysis
            # Define the independent variable (Income) and dependent variable (Poverty_Rate)
            X = data_cleaned[['Income']]
            y = data_cleaned['Poverty_Rate']

            # Add a constant to the independent variable
            X = sm.add_constant(X)

            # Fit the regression model
            model = sm.OLS(y, X).fit()

            # Print the model summary
            print(model.summary())
