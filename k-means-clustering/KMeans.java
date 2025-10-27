import java.util.*;

public class KMeans {
    private int k;
    private int maxIters;
    private double[][] centroids;
    
    public KMeans(int k, int maxIters) {
        this.k = k;
        this.maxIters = maxIters;
    }
    
    public int[] fit(double[][] X) {
        Random rand = new Random();
        centroids = new double[k][X[0].length];
        
        // Initialize centroids randomly
        for (int i = 0; i < k; i++) {
            int randomIndex = rand.nextInt(X.length);
            for (int j = 0; j < X[0].length; j++) {
                centroids[i][j] = X[randomIndex][j];
            }
        }
        
        for (int iter = 0; iter < maxIters; iter++) {
            int[] labels = new int[X.length];
            
            // Assign points to closest centroid
            for (int i = 0; i < X.length; i++) {
                double minDist = Double.MAX_VALUE;
                int label = 0;
                for (int j = 0; j < k; j++) {
                    double dist = 0;
                    for (int d = 0; d < X[0].length; d++) {
                        dist += Math.pow(X[i][d] - centroids[j][d], 2);
                    }
                    dist = Math.sqrt(dist);
                    if (dist < minDist) {
                        minDist = dist;
                        label = j;
                    }
                }
                labels[i] = label;
            }
            
            // Update centroids
            double[][] newCentroids = new double[k][X[0].length];
            int[] counts = new int[k];
            
            for (int i = 0; i < X.length; i++) {
                for (int j = 0; j < X[0].length; j++) {
                    newCentroids[labels[i]][j] += X[i][j];
                }
                counts[labels[i]]++;
            }
            
            for (int i = 0; i < k; i++) {
                if (counts[i] > 0) {
                    for (int j = 0; j < X[0].length; j++) {
                        newCentroids[i][j] /= counts[i];
                    }
                }
            }
            centroids = newCentroids;
        }
        
        // Final assignment
        int[] labels = new int[X.length];
        for (int i = 0; i < X.length; i++) {
            double minDist = Double.MAX_VALUE;
            int label = 0;
            for (int j = 0; j < k; j++) {
                double dist = 0;
                for (int d = 0; d < X[0].length; d++) {
                    dist += Math.pow(X[i][d] - centroids[j][d], 2);
                }
                dist = Math.sqrt(dist);
                if (dist < minDist) {
                    minDist = dist;
                    label = j;
                }
            }
            labels[i] = label;
        }
        return labels;
    }
    
    public static void main(String[] args) {
        KMeans kmeans = new KMeans(2, 100);
        double[][] X = {{1, 2}, {1, 4}, {1, 0}, {10, 2}, {10, 4}, {10, 0}};
        int[] labels = kmeans.fit(X);
        System.out.println(Arrays.toString(labels));
    }
}
