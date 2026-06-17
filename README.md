# House Prices Linear Regression Project


## Question
Can house prices be predicted using property features such as bedrooms, bathrooms, living area, lot size, condition, and year built?

The goal of this project is to build a Linear Regression model that predicts a property's sale price based on its available features.

## Model
I trained this model using SciKit_Learn's LinearRegression(). I split the features into X and y to represent the input and target features respectively. I split the data into training and test data with a 80/20 split.

## Model Evaluation
On average the model has an error of $167,887.78. The RMSE is 255889.84 meaning that the model makes some especially large errors on certain house. R-Squared is 0.375 meaning that the model explain about 37.5% of the variation in house prices, meaning it is abit better than predicting the average price.

## Data
The dataset used in this project was sourced from Kaggle:

Dataset: USA House Prices
Source: https://www.kaggle.com/datasets/fratzcan/usa-house-prices

This dataset was chosen because it is suitable for a beginner Linear Regression project. It contains one CSV file, has no missing values, and includes a clear target variable: Price.
