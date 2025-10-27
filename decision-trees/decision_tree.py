import numpy as np
from collections import Counter

class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
    
    def gini(self, y):
        counts = Counter(y)
        impurity = 1.0
        for count in counts.values():
            prob = count / len(y)
            impurity -= prob ** 2
        return impurity
    
    def split(self, X, y, feature, threshold):
        left_mask = X[:, feature] <= threshold
        return X[left_mask], X[~left_mask], y[left_mask], y[~left_mask]
    
    def best_split(self, X, y):
        best_gini = float('inf')
        best_feature, best_threshold = None, None
        
        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                X_left, X_right, y_left, y_right = self.split(X, y, feature, threshold)
                if len(y_left) == 0 or len(y_right) == 0:
                    continue
                
                gini = (len(y_left) * self.gini(y_left) + len(y_right) * self.gini(y_right)) / len(y)
                if gini < best_gini:
                    best_gini = gini
                    best_feature, best_threshold = feature, threshold
        
        return best_feature, best_threshold
    
    def build_tree(self, X, y, depth=0):
        if depth >= self.max_depth or len(np.unique(y)) == 1:
            return Counter(y).most_common(1)[0][0]
        
        feature, threshold = self.best_split(X, y)
        if feature is None:
            return Counter(y).most_common(1)[0][0]
        
        X_left, X_right, y_left, y_right = self.split(X, y, feature, threshold)
        
        return {
            'feature': feature,
            'threshold': threshold,
            'left': self.build_tree(X_left, y_left, depth + 1),
            'right': self.build_tree(X_right, y_right, depth + 1)
        }
    
    def fit(self, X, y):
        self.tree = self.build_tree(X, y)
    
    def predict_one(self, x, tree):
        if not isinstance(tree, dict):
            return tree
        
        if x[tree['feature']] <= tree['threshold']:
            return self.predict_one(x, tree['left'])
        else:
            return self.predict_one(x, tree['right'])
    
    def predict(self, X):
        return [self.predict_one(x, self.tree) for x in X]

# Test
X = np.array([[1, 2], [2, 3], [3, 1], [4, 2]])
y = np.array([0, 0, 1, 1])
model = DecisionTree()
model.fit(X, y)
print(model.predict([[2.5, 2.5]]))  # [1]
