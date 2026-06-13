# Linear Regression Project
## Data Science Project Lifecycle

This project follows a simple data science workflow:

Question → Data → Explore → Clean → Model → Evaluate → Improve → Explain

### 1. Question
Can house prices be predicted using property features such as bedrooms, bathrooms, living area, lot size, condition, and year built?

The goal of this project is to build a Linear Regression model that predicts a property's sale price based on its available features.

### 2. Data
The dataset used in this project was sourced from Kaggle:

Dataset: USA House Prices
Source: https://www.kaggle.com/datasets/fratzcan/usa-house-prices

This dataset was chosen because it is suitable for a beginner Linear Regression project. It contains one CSV file, has no missing values, and includes a clear target variable: Price.

### 3. Explore
After exploration of the dataset, I have confirmed that there are no missing values, and that the only thing that needs to be handled are the object types. This raises an important question: how should I handle object types? Should I encode them and if so how should I encode them? If I remove them, how should I remove them? It is important to handle this careful as to not introduce bais to the dataset.

### 4. Clean
The dataset contains the following object-type columns:
`date`, `street`, `city`, `statezip`, and `country`.

For version 1 of the model, I chose to keep the preprocessing simple.
The `date` column was converted into a numerical feature called `days_since_first_sale`. This represents how many days after the first recorded sale each property was sold. This is more useful than using the raw date string because Linear Regression requires numerical input features.

The remaining object-type columns were dropped for the first version of the model.

### 5. Model
I trained this model using SciKit_Learn's LinearRegression(). I split the features into X and y to represent the input and target features respectively. I split the data into training and test data with a 80/20 split.

### 6. Evaluate
On average the model has an error of $167,887.78. The RMSE is 255889.84 meaning that the model makes some especially large errors on certain house. R-Squared is 0.375 meaning that the model explain about 37.5% of the variation in house prices, meaning it is abit better than predicting the average price.

### 7. Improve
I would like to implement my own Linear Regression method without SciKit learn's library just using numpy.