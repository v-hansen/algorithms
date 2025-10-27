import numpy as np

class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
    
    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iters):
            distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
            labels = np.argmin(distances, axis=0)
            
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids
        
        return labels

# Test
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(k=2)
labels = kmeans.fit(X)
print(labels)  # [0 0 0 1 1 1]
