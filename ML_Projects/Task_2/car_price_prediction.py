import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
df = pd.read_csv('car_data.csv')

# Data Preprocessing - Checking for missing values
print("Missing values:\n", df.isnull().sum())

# Dropping duplicates if any
df = df.drop_duplicates()

# Selecting features - giving alphabetical_values a numbers
df['Fuel_Type'] = df['Fuel_Type'].map({'Petrol': 0, 'Diesel': 1, 'CNG': 2})
df['Seller_Type'] = df['Seller_Type'].map({'Dealer': 0, 'Individual': 1})
df['Transmission'] = df['Transmission'].map({'Manual': 0, 'Automatic': 1})

# Defining X and y
X = df.drop(['Car_Name', 'Selling_Price'], axis=1)
y = df['Selling_Price']

# Visualization
plt.scatter(df['Year'], df['Selling_Price'])
plt.xlabel('Year')
plt.ylabel('Selling Price')
plt.title('Year vs Selling Price')
plt.show()

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)

print("\nLinear Regression Results:")
print("MSE:", mean_squared_error(y_test, lr_preds))
print("R2 Score:", r2_score(y_test, lr_preds))

# Decision Tree Regressor Model
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)

print("\nDecision Tree Results:")
print("MSE:", mean_squared_error(y_test, dt_preds))
print("R2 Score:", r2_score(y_test, dt_preds))

# Comparing models
if r2_score(y_test, dt_preds) > r2_score(y_test, lr_preds):
    print("\nDecision Tree performed better.")
else:
    print("\nLinear Regression performed better.")
