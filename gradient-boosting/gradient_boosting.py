import numpy as np

class GradientBoosting:
    def __init__(self, n_estimators=10, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def fit(self, X, y):
        # Initialize with log odds
        self.initial_prediction = np.log(np.mean(y) / (1 - np.mean(y)))
        
        # Current predictions
        current_predictions = np.full(len(y), self.initial_prediction)
        
        for _ in range(self.n_estimators):
            # Calculate residuals (negative gradient)
            probabilities = self.sigmoid(current_predictions)
            residuals = y - probabilities
            
            # Fit a simple regression tree to residuals
            tree = self.fit_tree(X, residuals)
            self.trees.append(tree)
            
            # Update predictions
            tree_predictions = self.predict_tree(X, tree)
            current_predictions += self.learning_rate * tree_predictions
    
    def fit_tree(self, X, y):
        # Simple regression tree (just finds best split)
        best_mse = float('inf')
        best_feature, best_threshold = None, None
        
        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_mask = X[:, feature] <= threshold
                if np.sum(left_mask) == 0 or np.sum(~left_mask) == 0:
                    continue
                
                y_left, y_right = y[left_mask], y[~left_mask]
                left_pred = np.mean(y_left) if len(y_left) > 0 else 0
                right_pred = np.mean(y_right) if len(y_right) > 0 else 0
                
                mse = np.sum((y_left - left_pred) ** 2) + np.sum((y_right - right_pred) ** 2)
                
                if mse < best_mse:
                    best_mse = mse
                    best_feature, best_threshold = feature, threshold
        
        if best_feature is None:
            return {'prediction': np.mean(y)}
        
        left_mask = X[:, best_feature] <= best_threshold
        left_pred = np.mean(y[left_mask]) if np.sum(left_mask) > 0 else 0
        right_pred = np.mean(y[~left_mask]) if np.sum(~left_mask) > 0 else 0
        
        return {
            'feature': best_feature,
            'threshold': best_threshold,
            'left_pred': left_pred,
            'right_pred': right_pred
        }
    
    def predict_tree(self, X, tree):
        if 'prediction' in tree:
            return np.full(len(X), tree['prediction'])
        
        predictions = np.zeros(len(X))
        for i, x in enumerate(X):
            if x[tree['feature']] <= tree['threshold']:
                predictions[i] = tree['left_pred']
            else:
                predictions[i] = tree['right_pred']
        return predictions
    
    def predict(self, X):
        predictions = np.full(len(X), self.initial_prediction)
        
        for tree in self.trees:
            tree_predictions = self.predict_tree(X, tree)
            predictions += self.learning_rate * tree_predictions
        
        probabilities = self.sigmoid(predictions)
        return (probabilities >= 0.5).astype(int)

# Test
X = np.array([[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = GradientBoosting(n_estimators=5)
model.fit(X, y)
print(model.predict([[2, 2], [7, 6]]))  # [0, 1]
