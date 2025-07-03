import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])  # y = 2x + 1

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

w = model.coef_[0]  # Get the slope (weight)
b = model.intercept_  # Get the intercept (bias)

# Print the coefficients
print(f"Weight: {w}, Bias: {b}")

# Plot the results
plt.scatter(X, y, label="Data")
plt.plot(X, model.predict(X), color="red", label="Model")
plt.legend()
plt.show()