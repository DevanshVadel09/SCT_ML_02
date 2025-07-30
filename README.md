# SCT_ML_02

# Mall Customer Spending Analysis

## Overview

This project analyzes customer spending patterns at a shopping mall based on demographic factors including age, gender, and annual income. The analysis provides insights into customer behavior and spending habits to help businesses make data-driven decisions for marketing strategies and customer segmentation.

## Dataset Description

The dataset contains customer information with the following features:

- **Customer ID**: Unique identifier for each customer
- **Gender**: Customer's gender (Male/Female)
- **Age**: Customer's age in years
- **Annual Income**: Customer's yearly income (in k$)
- **Spending Score**: Score assigned based on customer spending behavior and purchasing data (1-100)

## Project Objectives

- Analyze spending patterns across different demographic groups
- Identify relationships between age, gender, income, and spending behavior
- Segment customers based on their characteristics
- Provide actionable insights for targeted marketing strategies
- Visualize trends and patterns in customer data

## Key Features

### Data Analysis
- Exploratory Data Analysis (EDA) of customer demographics
- Statistical analysis of spending patterns by gender and age groups
- Correlation analysis between income and spending scores
- Distribution analysis of key variables

### Customer Segmentation
- K-means clustering to identify distinct customer segments
- Analysis of high-value vs. low-value customers
- Age-based customer categorization
- Income-based customer profiling

### Visualizations
- Gender-wise spending distribution
- Age vs. spending score scatter plots
- Income vs. spending correlation heatmaps
- Customer segment visualization using clustering
- Demographic breakdown charts

## Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Data visualization
- **Scikit-learn**: Machine learning algorithms (clustering)
- **Jupyter Notebook**: Development environment

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mall-customer-analysis.git

# Navigate to project directory
cd mall-customer-analysis

# Install required packages
pip install -r requirements.txt
```

## Usage

```python
# Run the main analysis
python customer_analysis.py

# Or open the Jupyter notebook
jupyter notebook Mall_Customer_Analysis.ipynb
```

## Key Findings

### Gender-Based Insights
- Analysis of spending differences between male and female customers
- Identification of gender-specific purchasing patterns

### Age Demographics
- Spending behavior across different age groups
- Peak spending age ranges identification

### Income Correlation
- Relationship between annual income and spending scores
- Identification of high-income vs. high-spending customers

### Customer Segments
- Distinct customer clusters based on demographics and spending
- Characteristics of each customer segment

## File Structure

```
mall-customer-analysis/
│
├── data/
│   └── Mall_Customers.csv
├── notebooks/
│   └── Mall_Customer_Analysis.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── analysis.py
│   └── visualization.py
├── results/
│   ├── plots/
│   └── customer_segments.csv
├── requirements.txt
└── README.md
└── app.py

```

## Results and Insights

The analysis reveals several key insights:

1. **Customer Segmentation**: Identified 5 distinct customer segments with unique characteristics
2. **Spending Patterns**: Strong correlation between certain demographic factors and spending behavior
3. **Target Demographics**: Specific age and income groups show higher spending potential
4. **Marketing Opportunities**: Clear segments for targeted marketing campaigns

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- Dataset source: [Mention the source if applicable]
- Inspiration from retail analytics and customer behavior studies
- Thanks to the open-source community for the tools and libraries used

---

*This project demonstrates the application of data science techniques in retail analytics and customer behavior analysis.*
