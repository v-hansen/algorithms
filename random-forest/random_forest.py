import numpy as np
from collections import Counter

class SimpleDecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
    
    def gini(self, y):
        counts = Counter(y)
        impurity = 1.0
        for count in counts.values():
            prob = count / len(y)
            impurity -= prob ** 2
        return impurity
    
    def fit(self, X, y, depth=0):
        if depth >= self.max_depth or len(np.unique(y)) == 1:
            return Counter(y).most_common(1)[0][0]
        
        best_gini = float('inf')
        best_feature, best_threshold = None, None
        
        # Random feature selection
        n_features = int(np.sqrt(X.shape[1]))
        features = np.random.choice(X.shape[1], n_features, replace=False)
        
        for feature in features:
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_mask = X[:, feature] <= threshold
                if np.sum(left_mask) == 0 or np.sum(~left_mask) == 0:
                    continue
                
                y_left, y_right = y[left_mask], y[~left_mask]
                gini = (len(y_left) * self.gini(y_left) + len(y_right) * self.gini(y_right)) / len(y)
                
                if gini < best_gini:
                    best_gini = gini
                    best_feature, best_threshold = feature, threshold
        
        if best_feature is None:
            return Counter(y).most_common(1)[0][0]
        
        left_mask = X[:, best_feature] <= best_threshold
        self.feature = best_feature
        self.threshold = best_threshold
        self.left = SimpleDecisionTree(self.max_depth).fit(X[left_mask], y[left_mask], depth + 1)
        self.right = SimpleDecisionTree(self.max_depth).fit(X[~left_mask], y[~left_mask], depth + 1)
        return self
    
    def predict_one(self, x):
        if not hasattr(self, 'feature'):
            return self
        
        if x[self.feature] <= self.threshold:
            return self.left.predict_one(x) if hasattr(self.left, 'predict_one') else self.left
        else:
            return self.right.predict_one(x) if hasattr(self.right, 'predict_one') else self.right

class RandomForest:
    def __init__(self, n_trees=10, max_depth=3):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []
    
    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            # Bootstrap sampling
            indices = np.random.choice(len(X), len(X), replace=True)
            X_sample, y_sample = X[indices], y[indices]
            
            tree = SimpleDecisionTree(self.max_depth)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)
    
    def predict(self, X):
        predictions = []
        for x in X:
            tree_predictions = [tree.predict_one(x) for tree in self.trees]
            prediction = Counter(tree_predictions).most_common(1)[0][0]
            predictions.append(prediction)
        return predictions

# Test
X = np.array([[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = RandomForest(n_trees=5)
model.fit(X, y)
print(model.predict([[2, 2], [7, 6]]))  # [0, 1]
