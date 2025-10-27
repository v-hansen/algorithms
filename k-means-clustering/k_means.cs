using System;
using System.Linq;

class KMeans {
    private int k;
    private int maxIters;
    private double[,] centroids;
    
    public KMeans(int k = 3, int maxIters = 100) {
        this.k = k;
        this.maxIters = maxIters;
    }
    
    public int[] Fit(double[,] X) {
        Random rand = new Random();
        int nSamples = X.GetLength(0);
        int nFeatures = X.GetLength(1);
        
        centroids = new double[k, nFeatures];
        
        // Initialize centroids randomly
        for (int i = 0; i < k; i++) {
            int randomIdx = rand.Next(nSamples);
            for (int j = 0; j < nFeatures; j++) {
                centroids[i, j] = X[randomIdx, j];
            }
        }
        
        for (int iter = 0; iter < maxIters; iter++) {
            int[] labels = new int[nSamples];
            
            // Assign points to closest centroid
            for (int i = 0; i < nSamples; i++) {
                double minDist = double.MaxValue;
                int label = 0;
                for (int j = 0; j < k; j++) {
                    double dist = 0;
                    for (int d = 0; d < nFeatures; d++) {
                        dist += Math.Pow(X[i, d] - centroids[j, d], 2);
                    }
                    if (dist < minDist) {
                        minDist = dist;
                        label = j;
                    }
                }
                labels[i] = label;
            }
            
            // Update centroids
            double[,] newCentroids = new double[k, nFeatures];
            int[] counts = new int[k];
            
            for (int i = 0; i < nSamples; i++) {
                for (int j = 0; j < nFeatures; j++) {
                    newCentroids[labels[i], j] += X[i, j];
                }
                counts[labels[i]]++;
            }
            
            for (int i = 0; i < k; i++) {
                if (counts[i] > 0) {
                    for (int j = 0; j < nFeatures; j++) {
                        newCentroids[i, j] /= counts[i];
                    }
                }
            }
            centroids = newCentroids;
        }
        
        // Final assignment
        int[] finalLabels = new int[nSamples];
        for (int i = 0; i < nSamples; i++) {
            double minDist = double.MaxValue;
            int label = 0;
            for (int j = 0; j < k; j++) {
                double dist = 0;
                for (int d = 0; d < nFeatures; d++) {
                    dist += Math.Pow(X[i, d] - centroids[j, d], 2);
                }
                if (dist < minDist) {
                    minDist = dist;
                    label = j;
                }
            }
            finalLabels[i] = label;
        }
        return finalLabels;
    }
    
    static void Main() {
        var X = new double[,] {{1, 2}, {1, 4}, {1, 0}, {10, 2}, {10, 4}, {10, 0}};
        var kmeans = new KMeans(2);
        var labels = kmeans.Fit(X);
        Console.WriteLine(string.Join(" ", labels));
    }
}
