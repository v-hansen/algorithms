import numpy as np

class LinearRegression:
    def __init__(self):
        self.w = None
        self.b = None
    
    def fit(self, X, y):
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        self.w = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
        self.b = y_mean - self.w * X_mean
    
    def predict(self, X):
        return self.w * X + self.b

# Test
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression()
model.fit(X, y)
print(model.predict([6]))  # [12]
