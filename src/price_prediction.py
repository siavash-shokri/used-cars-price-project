import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv("used-cars-price-project/data/used_cars_cleaned.csv")

plt.figure(figsize=(8,5))
sns.histplot(df["price"], bins=30)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

x = df["milage"]
y = df["price"]
plt.scatter(x,y, color="blue", s=100)
plt.title("Price vs Mileage")
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.show()

x = df["model_year"]
y = df["price"]
plt.scatter(x,y, color="blue", s=100)
plt.title("Price vs Model Year")
plt.xlabel("Model Year")
plt.ylabel("Price")
plt.show()

brandRel = df.groupby("brand")["price"].median().nlargest(10)
x = brandRel.index.tolist()
y = brandRel.tolist()
plt.barh(x,y, color="skyblue")
plt.title("Top 10 Brands by Median Price")
plt.xlabel("Median Price")
plt.ylabel("Brands")
plt.ticklabel_format(style="plain", axis="x")
plt.show()

fuelRel = df.groupby("fuel_type")["price"].median()
x = fuelRel.index.tolist()
y = fuelRel.tolist()
plt.barh(x,y, color="skyblue")
plt.title("Fuel Type vs Median Price")
plt.xlabel("Median Price")
plt.ylabel("Fuel Types")
plt.ticklabel_format(style="plain", axis="x")
plt.show()

df["fuel_type"] = df["fuel_type"].replace("–", pd.NA).replace("not supported", pd.NA)
df[["fuel_type", "accident"]] = df[["fuel_type", "accident"]].fillna("unknown")

hppattern = r"(\d+(?:\.\d+)?)\s*HP"
dpattern = r"(\d+(?:\.\d+)?)\s*(?:L|Liter)"
cpattern = r"(?i)(\d+)\s*Cylinder|(?:I|V|H|W|Flat\s*|Straight\s*)-?(\d+)"
horsepower = df["engine"].str.extract(hppattern, expand=False)
horsepower = pd.to_numeric(horsepower, errors="coerce")
displacement = df["engine"].str.extract(dpattern, expand=False)
displacement = pd.to_numeric(displacement, errors="coerce")
cylinders = df["engine"].str.extract(cpattern)
cylinders = cylinders[0].fillna(cylinders[1])
cylinders = pd.to_numeric(cylinders, errors="coerce")
is_electric = df["engine"].str.contains("Electric", case= False, na= False)
is_hydrogen = df["engine"].str.contains("Hydrogen", case= False, na= False)
is_rotary = df["engine"].str.contains("Rotary", case= False, na= False)
engine_info= pd.DataFrame({
    "cylinders":    cylinders,
    "displacement": displacement,
    "horsepower":   horsepower,
    "is_electric":  is_electric,
    "is_hydrogen": is_hydrogen,
    "is_rotary": is_rotary
})
df = pd.concat([df, engine_info], axis=1)
df = df.drop(columns=["engine", 
                      "ext_col", 
                      "int_col", 
                      "clean_title", 
                      "id"])

x = df.drop(columns=["price"]) 
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                            test_size=0.2, 
                                            random_state=42)

categorical_columns = ["brand", 
                       "model", 
                       "fuel_type", 
                       "transmission", 
                       "accident"]
enc = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

enc_x_train_data = enc.fit_transform(x_train[categorical_columns])
enc_x_train_df = pd.DataFrame(enc_x_train_data, 
                              columns=enc.get_feature_names_out(categorical_columns), 
                              index=x_train.index)
x_train = x_train.drop(columns=categorical_columns)
x_train = pd.concat([x_train, enc_x_train_df], axis=1)
m_cylinders, m_displacement, m_horsepower = x_train[["cylinders", "displacement", "horsepower"]].median()
x_train["cylinders"] = x_train["cylinders"].fillna(m_cylinders)
x_train["displacement"] = x_train["displacement"].fillna(m_displacement)
x_train["horsepower"] = x_train["horsepower"].fillna(m_horsepower)

enc_x_test_data = enc.transform(x_test[categorical_columns])
enc_x_test_df = pd.DataFrame(enc_x_test_data, 
                             columns=enc.get_feature_names_out(categorical_columns), 
                             index=x_test.index)
x_test = x_test.drop(columns= categorical_columns)
x_test = pd.concat([x_test, enc_x_test_df], axis=1)
x_test["cylinders"] = x_test["cylinders"].fillna(m_cylinders)
x_test["displacement"] = x_test["displacement"].fillna(m_displacement)
x_test["horsepower"] = x_test["horsepower"].fillna(m_horsepower)

rf_reg = RandomForestRegressor(n_estimators=200, random_state=42)
rf_reg.fit(x_train, y_train)
y_pred = rf_reg.predict(x_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))

importances = pd.Series(rf_reg.feature_importances_, 
                        index=x_train.columns).sort_values(ascending=False)
top10 = importances.head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top10.values, y=top10.index)
plt.title("Top 10 Feature Importance from Random Forest Regressor")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()