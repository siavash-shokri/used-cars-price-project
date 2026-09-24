import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import HistGradientBoostingRegressor

df = pd.read_csv("data/used_cars_cleaned.csv")

df["fuel_type"] = df["fuel_type"].replace("–", pd.NA).replace("not supported", pd.NA)
df[["fuel_type", "accident"]] = df[["fuel_type", "accident"]].fillna("unknown")

x = df.drop(columns=["price", "id", "engine", "ext_col", "int_col", "clean_title"])
y = df['price']

x_train,x_test,y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) 

categorical_columns = ["brand", "model", "fuel_type", "transmission", "accident"]
enc = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
enc_x_train_data = enc.fit_transform(x_train[categorical_columns])
enc_x_train_df = pd.DataFrame(enc_x_train_data, columns=enc.get_feature_names_out(categorical_columns), index=x_train.index)
f_x_train = x_train.drop(columns=categorical_columns)
f_x_train = pd.concat([f_x_train, enc_x_train_df], axis=1)

enc_x_test_data = enc.transform(x_test[categorical_columns])
enc_x_test_df = pd.DataFrame(enc_x_test_data, columns=enc.get_feature_names_out(categorical_columns), index=x_test.index)
f_x_test = x_test.drop(columns= categorical_columns)
f_x_test = pd.concat([f_x_test, enc_x_test_df], axis=1)


regr = LinearRegression()
regr.fit(f_x_train, y_train)
y_pred = regr.predict(f_x_test)

mae = mean_absolute_error(y_true=y_test, y_pred= y_pred)
rmse = np.sqrt(mean_squared_error(y_true=y_test, y_pred= y_pred))
r2 = r2_score(y_test, y_pred)
print("Linear Regression Results: ")
print("MAE: ",mae)
print("RMSE: ",rmse)
print("R^2: ", r2)


dtr = DecisionTreeRegressor(max_depth=16,random_state=42)
dtr.fit(f_x_train, y_train)
y_pred = dtr.predict(f_x_test)

mae = mean_absolute_error(y_true=y_test, y_pred= y_pred)
rmse = np.sqrt(mean_squared_error(y_true=y_test, y_pred= y_pred))
r2 = r2_score(y_test, y_pred)
print("Decision Tree Regressor Results: ")
print("Max depth = 16")
print("MAE: ",mae)
print("RMSE: ",rmse)
print("R^2: ", r2)
y_t_pred = dtr.predict(f_x_train)
t_r2 = r2_score(y_train, y_t_pred)
print("Training R^2: ", t_r2)

hgbr = HistGradientBoostingRegressor(learning_rate=0.1, max_iter=300,random_state=42)
hgbr.fit(f_x_train, y_train)
y_pred = hgbr.predict(f_x_test)
mae = mean_absolute_error(y_true=y_test, y_pred= y_pred)
rmse = np.sqrt(mean_squared_error(y_true=y_test, y_pred= y_pred))
r2 = r2_score(y_test, y_pred)
print("Hist Gradient Boosting Regressor Results: ")
print("MAE: ",mae)
print("RMSE: ",rmse)
print("R^2: ", r2)