import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.01, max_iters=1000):
        self.lr = lr
        self.max_iters = max_iters
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
    
    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        self.b = 0
        
        for _ in range(self.max_iters):
            z = X.dot(self.w) + self.b
            h = self.sigmoid(z)
            
            dw = X.T.dot(h - y) / len(y)
            db = np.sum(h - y) / len(y)
            
            self.w -= self.lr * dw
            self.b -= self.lr * db
    
    def predict(self, X):
        return (self.sigmoid(X.dot(self.w) + self.b) >= 0.5).astype(int)

# Test
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])
model = LogisticRegression()
model.fit(X, y)
print(model.predict([[2.5, 3.5]]))  # [1]
