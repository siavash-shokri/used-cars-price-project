# Used Car Market Analysis & Price Prediction

## Overview

This project analyzes a dataset of used-car listings and builds a machine learning model to predict a car's listing price.

The project combines SQL, Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn to cover the process from data preparation and exploratory analysis to feature engineering, machine learning, model evaluation, and interpretation.

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
3. Performed exploratory data analysis using Pandas, Matplotlib, and Seaborn.
4. Examined relationships between price and features such as mileage and model year.
5. Extracted numerical engine features including horsepower, displacement, and cylinder count.
6. Created indicators for electric, hydrogen, and rotary engines.
7. Encoded categorical features using One-Hot Encoding.
8. Split the data into training and testing sets.
9. Trained a Random Forest regression model.
10. Evaluated the model using MAE, RMSE, and R².
11. Analyzed feature importance to understand which features contributed most to the model's predictions.

## Exploratory Analysis

The exploratory analysis examined the distribution of listing prices and relationships between price and vehicle characteristics.

Visualizations included:

- Price distribution
- Price vs. mileage
- Price vs. model year
- Median price by brand
- Median price by fuel type
- Accident history and median price comparison

The correlation between price and mileage was approximately **-0.306**, while the correlation between price and model year was approximately **0.199** in this dataset.

## Machine Learning Models

Several regression models were tested during development:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | $19,563 | $32,521 | 0.548 |
| Decision Tree Regressor | $14,487 | $27,110 | 0.686 |
| HistGradientBoosting Regressor | $18,315 | $35,867 | 0.450 |
| Random Forest Regressor | $8,763 | $19,009 | 0.846 |

The final model uses a Random Forest Regressor with 200 trees.

### Final Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest Regressor | $8,763 | $19,008 | 0.845 |

the Random Forest produced the strongest reported test metrics among the models listed.

## Feature Engineering

The original `engine` column contained semi-structured text. Numerical and categorical information was extracted from it to create:

- Horsepower
- Engine displacement
- Cylinder count
- Electric engine indicator
- Hydrogen engine indicator
- Rotary engine indicator

## Feature Importance

Feature importance from the Random Forest model showed that mileage was the most influential feature among the model inputs.

Vehicle-specific model categories and engine characteristics such as cylinder count, displacement, and horsepower also appeared among the most influential features.

Feature importance describes the model's use of features for prediction and should not be interpreted as evidence of causation.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
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
│   └── price_prediction.py
└── README.md
```

## Limitations

The dataset contains a large number of different vehicle models, including many models with relatively few listings. Some engine information is incomplete or stored in inconsistent text formats, so the extracted engine features contain some missing values that are imputed during preprocessing.

The dataset also contains a small number of unusually expensive listings, which can have a large effect on error metrics such as RMSE.

The final model was evaluated on a held-out test set, so the reported results should be interpreted as performance on this dataset rather than as a general pricing system for all used vehicles.

## Future Improvements

Possible improvements include:

- More systematic handling of rare vehicle models
- More advanced preprocessing using Scikit-learn pipelines
- Testing additional feature engineering approaches
- Evaluating the model using more extensive cross-validation
- Investigating additional vehicle attributes if more complete data becomes available