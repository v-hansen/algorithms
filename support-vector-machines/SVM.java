public class SVM {
    private double lr;
    private double lambdaParam;
    private int nIters;
    private double[] w;
    private double b;
    
    public SVM(double lr, double lambdaParam, int nIters) {
        this.lr = lr;
        this.lambdaParam = lambdaParam;
        this.nIters = nIters;
    }
    
    public SVM() {
        this(0.001, 0.01, 1000);
    }
    
    public void fit(double[][] X, int[] y) {
        // Convert labels to -1 and 1
        int[] y_ = new int[y.length];
        for (int i = 0; i < y.length; i++) {
            y_[i] = y[i] <= 0 ? -1 : 1;
        }
        
        int nFeatures = X[0].length;
        w = new double[nFeatures];
        b = 0;
        
        for (int iter = 0; iter < nIters; iter++) {
            for (int i = 0; i < X.length; i++) {
                double[] xi = X[i];
                int yi = y_[i];
                
                boolean condition = yi * (dotProduct(xi, w) - b) >= 1;
                
                if (condition) {
                    for (int j = 0; j < w.length; j++) {
                        w[j] -= lr * (2 * lambdaParam * w[j]);
                    }
                } else {
                    for (int j = 0; j < w.length; j++) {
                        w[j] -= lr * (2 * lambdaParam * w[j] - xi[j] * yi);
                    }
                    b -= lr * yi;
                }
            }
        }
    }
    
    private double dotProduct(double[] a, double[] b) {
        double sum = 0;
        for (int i = 0; i < a.length; i++) {
            sum += a[i] * b[i];
        }
        return sum;
    }
    
    public int[] predict(double[][] X) {
        int[] predictions = new int[X.length];
        
        for (int i = 0; i < X.length; i++) {
            double approx = dotProduct(X[i], w) - b;
            int sign = approx >= 0 ? 1 : -1;
            predictions[i] = (sign + 1) / 2; // Convert back to 0,1
        }
        
        return predictions;
    }
    
    public static void main(String[] args) {
        double[][] X = {{1, 2}, {2, 3}, {3, 1}, {6, 5}, {7, 7}, {8, 6}};
        int[] y = {0, 0, 0, 1, 1, 1};
        
        SVM model = new SVM();
        model.fit(X, y);
        int[] predictions = model.predict(new double[][]{{2, 2}, {7, 6}});
        
        for (int pred : predictions) {
            System.out.print(pred + " ");
        }
        System.out.println(); // [0, 1]
    }
}
