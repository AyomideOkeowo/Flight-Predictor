# Flight-Predictor
# Project Summary
This project involves building and deploying a machine learning model to predict flight ticket prices based on various features such as airline, route, duration, and timing. The model was developed using several regression algorithms and exposed via a Flask API. The application was deployed to Render, enabling real time predictions through a RESTful endpoint.

# Tools & Libraries 
## Python Libraries
Flask – Web framework for building the API

Flask-CORS – Handling cross origin resource sharing

Scikit-learn – Model training and evaluation

CatBoost – Gradient boosting model

XGBoost – Extreme Gradient Boosting

LightGBM – Light Gradient Boosting

Pandas – Data manipulation

NumPy – Numerical operations

Matplotlib & Seaborn – Exploratory data analysis (EDA)

Cufflinks & Plotly (Chart Studio) – Interactive visualisations

# Deployment
Gunicorn – WSGI HTTP server used in production

Render – Hosting platform for deploying the Flask API

# Project Overview
## Exploratory Data Analysis (EDA)
Performed thorough EDA using Seaborn, Matplotlib, and Plotly to understand key trends and patterns.

Investigated features like airline type, travel duration, number of stops, and departure/arrival times.

Visualised distributions, correlations, and categorical impacts on price.

## Feature Engineering
Extracted useful features such as:

Journey day and month

Flight duration in minutes

Total stops as numerical input

Converted time and date formats for consistency.

## Data Encoding
Applied One-Hot Encoding for categorical variables such as airlines and source/destination cities.

## Model Building & Tuning
Trained and evaluated multiple regression models:

ExtraTreesRegressor

RandomForestRegressor

CatBoostRegressor

LightGBM

XGBoost

Hyperparameter tuning was performed using GridSearchCV and cross validation techniques to improve model performance.

Evaluation metrics included R² score, MAE, and RMSE.

## API Development with Flask
Wrapped the trained model inside a Flask API.

Created routes to accept flight data via POST requests and return predicted prices.

Integrated CORS to ensure compatibility with front end or external applications.

## Deployment to Render
Configured Gunicorn as the WSGI server for production readiness.

Deployed the Flask API to Render, providing a live endpoint for real time predictions.
