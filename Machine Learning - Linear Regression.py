# Simple linear regression from scratch
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None
    
    def fit(self, X, y):
        # Calculate slope and intercept using least squares
        n = len(X)
        mean_x = np.mean(X)
        mean_y = np.mean(y)
        
        numerator = np.sum((X - mean_x) * (y - mean_y))
        denominator = np.sum((X - mean_x) ** 2)
        
        self.slope = numerator / denominator
        self.intercept = mean_y - self.slope * mean_x
    
    def predict(self, X):
        return self.slope * X + self.intercept
    
    def score(self, X, y):
        # R-squared score
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - (ss_res / ss_tot)

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2.5 * X.squeeze() + 1.5 + np.random.randn(100) * 2

# Train model
model = LinearRegression()
model.fit(X.squeeze(), y)

# Predict and plot
plt.scatter(X, y, alpha=0.7, label='Actual Data')
plt.plot(X, model.predict(X.squeeze()), color='red', label='Regression Line')
plt.title(f'Linear Regression: y = {model.slope:.2f}x + {model.intercept:.2f}')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"R-squared: {model.score(X.squeeze(), y):.3f}")
