# Used Car Market Analysis & Price Prediction

## Overview

This project analyzes a dataset of used-car listings and builds machine learning models to predict a car's listing price.

The project combines SQL, Python, Pandas, NumPy, and Scikit-learn to cover the full process from data preparation and exploratory analysis to machine learning and model evaluation.

## Dataset

The dataset contains 4,009 used-car listings with information such as:

- Brand
- Model
- Model year
- Mileage
- Fuel type
- Engine
- Transmission
- Accident history
- Listing price

The `price` column represents the listed market price in the dataset, not a verified final sale price.

## Project Workflow

1. Loaded and cleaned the raw dataset.
2. Stored and explored the data using PostgreSQL and SQL.
3. Performed exploratory data analysis with Pandas and Matplotlib.
4. Examined relationships between price and features such as mileage and model year.
5. Encoded categorical features using One-Hot Encoding.
6. Split the data into training and testing sets.
7. Trained and compared three regression models.
8. Evaluated the models using MAE, RMSE, and R².

## Exploratory Analysis

Some of the analysis performed included:

- Price vs. mileage
- Price vs. model year
- Median price by brand
- Median price by fuel type
- Brand and feature frequency analysis
- Accident history and median price comparison

The correlation between price and mileage was approximately **-0.306**, while the correlation between price and model year was approximately **0.199** in this dataset.

## Machine Learning Models

Three regression models were evaluated:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | $19,563 | $32,521 | 0.548 |
| Decision Tree Regressor | $14,487 | $27,110 | 0.686 |
| HistGradientBoosting Regressor | $18,315 | $35,867 | 0.450 |

The Decision Tree Regressor with a maximum depth of 16 produced the highest test-set R² among the models tested.

Its training R² was approximately **0.966**, compared with a test R² of **0.686**, indicating that the model fits the training data considerably better than unseen test data.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- PostgreSQL
- SQL

## Project Structure

```text
used-cars-price-project/
├── data/
│   ├── used_cars.csv
│   └── used_cars_cleaned.csv
├── sql/
│   └── sql_project.sql
├── src/
│   └── pandas_project.py
└── README.md

## Limitations

The dataset contains a large number of different vehicle models, including many models with relatively few listings. Some vehicle information, such as engine specifications, is stored as text and was not included in the first version of the machine learning model.

The model was evaluated using a single train/test split, so the results should be considered a first modeling baseline rather than a production-ready pricing system.

## Future Improvements

Possible improvements include:
- Extracting numerical features such as horsepower and engine displacement from the engine column.
- Exploring additional feature engineering.
- Testing additional regression models.
- Using cross-validation for more robust model evaluation. 
- Improving the handling of rare vehicle models.

