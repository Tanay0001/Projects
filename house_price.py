# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Sample dataset (replace with actual data)
data = {
    'size': [750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200],
    'bedrooms': [2, 2, 3, 3, 3, 4, 4, 4, 4, 5],
    'age': [12, 15, 10, 10, 8, 6, 5, 4, 3, 1],
    'price': [150000, 170000, 180000, 190000, 210000, 220000, 240000, 250000, 260000, 300000]
}

# Converting to DataFrame
df = pd.DataFrame(data)

# Features (size, bedrooms, age) and target (price)
X = df[['size', 'bedrooms', 'age']]
y = df['price']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the model
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Optional: Plotting actual vs predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
