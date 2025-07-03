import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])  # y = 2x + 1


def predict(w, b, X):
    return w * X + b


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def train(X, y, learning_rate=0.01, epochs=1000):
    w, b = 0.0, 0.0  # Initialize weights and bias as 0 at start
    n = len(X)

    for epoch in range(epochs):
        y_predict = predict(w, b, X)
        loss = y_predict - y  # Calculate the loss (difference between predicted and actual values)
        dw = (-2 / n) * np.sum(X * loss)  # Gradient with respect to w
        # Gradient with respect to b
        db = (-2 / n) * np.sum(loss)

        w = w + learning_rate * dw
        b = b + learning_rate * db

        if epoch % 100 == 0:
            print(f"Epoch {epoch}: MSE = {mse(y, y_predict):.4f}")

    return w, b


# Train the model
w, b = train(X, y)
print(f"Final weights: {w}, bias: {b}")

# Plot
plt.scatter(X, y, label="Data")
plt.plot(X, predict(w, b, X), color="red", label="Model")
plt.legend()
plt.show()
