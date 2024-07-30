# Analyzing Poverty Data Worldwide

## Project Description

This project aims to analyze poverty data worldwide and visualize the key insights. The analysis focuses on understanding the relationship between income levels and poverty rates across different regions and over time. The project uses data from the World Bank and includes various statistical analyses and visualizations to uncover trends and correlations in the data.

## Data Description

The dataset used in this project is obtained from the World Bank's Poverty and Equity Database. It includes the following key columns:

- `Country`: The name of the country.
- `Country Code`: The ISO code of the country.
- `Region`: The region to which the country belongs.
- `Income Group`: The income group classification of the country.
- `Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)`: The percentage of the population living below the international poverty line of $1.90 a day (2011 PPP).
- `GNI per capita, Atlas method (current US$)`: The Gross National Income per capita in current US dollars.
- `Year`: The year of the data record.

The dataset also includes additional columns related to various economic indicators and metadata.

1. ## Project Structure

- `main.py`: The main script for loading, cleaning, analyzing, and visualizing the poverty data.
- `PovStatsCountry.csv`: The dataset file (you will need to download and place this file in the project directory).

2. **Install Dependencies**
    Ensure you have Python installed. Then, install the required Python libraries:
    ```sh
    pip install pandas matplotlib seaborn statsmodels scipy
    ```

3. **Download the Data**
    Download the `PovStatsCountry.csv` file from the World Bank's Poverty and Equity Database and place it in the project directory.

4. **Run the Analysis**
    Execute the `main.py` script to perform the analysis and generate visualizations:
    ```sh
    python main.py
    ```

## Analysis and Visualizations

The analysis includes the following steps:

1. **Data Loading and Cleaning**: Load the data from the CSV file and clean it by removing rows with missing values in key columns.

2. **Summary Statistics**: Generate summary statistics for the cleaned dataset.

3. **Visualizations**:
    - Histogram of income levels.
    - Box plot of poverty rates by region.
    - Heatmap of the correlation matrix.
    - Scatter plot of poverty rate vs. income.
    - Line plot of poverty rate over years by region.

4. **Statistical Analysis**:
    - Calculate the Pearson correlation between income and poverty rate.
    - Perform a linear regression analysis to understand the relationship between income and poverty rate.
