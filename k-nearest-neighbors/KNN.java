import java.util.*;

public class KNN {
    private int k;
    private double[][] X_train;
    private int[] y_train;
    
    public KNN(int k) {
        this.k = k;
    }
    
    public void fit(double[][] X, int[] y) {
        this.X_train = X;
        this.y_train = y;
    }
    
    private double euclideanDistance(double[] x1, double[] x2) {
        double sum = 0;
        for (int i = 0; i < x1.length; i++) {
            sum += Math.pow(x1[i] - x2[i], 2);
        }
        return Math.sqrt(sum);
    }
    
    public int[] predict(double[][] X) {
        int[] predictions = new int[X.length];
        
        for (int i = 0; i < X.length; i++) {
            List<Distance> distances = new ArrayList<>();
            
            for (int j = 0; j < X_train.length; j++) {
                double dist = euclideanDistance(X[i], X_train[j]);
                distances.add(new Distance(dist, y_train[j]));
            }
            
            distances.sort(Comparator.comparingDouble(d -> d.distance));
            
            Map<Integer, Integer> counts = new HashMap<>();
            for (int j = 0; j < k; j++) {
                int label = distances.get(j).label;
                counts.put(label, counts.getOrDefault(label, 0) + 1);
            }
            
            predictions[i] = counts.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .get().getKey();
        }
        
        return predictions;
    }
    
    private static class Distance {
        double distance;
        int label;
        
        Distance(double distance, int label) {
            this.distance = distance;
            this.label = label;
        }
    }
    
    public static void main(String[] args) {
        double[][] X_train = {{1, 2}, {2, 3}, {3, 1}, {6, 5}, {7, 7}, {8, 6}};
        int[] y_train = {0, 0, 0, 1, 1, 1};
        double[][] X_test = {{2, 2}, {7, 6}};
        
        KNN model = new KNN(3);
        model.fit(X_train, y_train);
        int[] predictions = model.predict(X_test);
        System.out.println(Arrays.toString(predictions)); // [0, 1]
    }
}
