public class LogisticRegression {
    private double[] w;
    private double b;
    private double lr;
    private int maxIters;
    
    public LogisticRegression(double lr, int maxIters) {
        this.lr = lr;
        this.maxIters = maxIters;
    }
    
    private double sigmoid(double z) {
        return 1.0 / (1.0 + Math.exp(-Math.max(-500, Math.min(500, z))));
    }
    
    public void fit(double[][] X, int[] y) {
        w = new double[X[0].length];
        b = 0;
        
        for (int iter = 0; iter < maxIters; iter++) {
            double[] dw = new double[w.length];
            double db = 0;
            
            for (int i = 0; i < X.length; i++) {
                double z = b;
                for (int j = 0; j < w.length; j++) z += X[i][j] * w[j];
                double h = sigmoid(z);
                double error = h - y[i];
                
                for (int j = 0; j < w.length; j++) dw[j] += error * X[i][j];
                db += error;
            }
            
            for (int j = 0; j < w.length; j++) w[j] -= lr * dw[j] / X.length;
            b -= lr * db / X.length;
        }
    }
    
    public int predict(double[] x) {
        double z = b;
        for (int j = 0; j < w.length; j++) z += x[j] * w[j];
        return sigmoid(z) >= 0.5 ? 1 : 0;
    }
    
    public static void main(String[] args) {
        LogisticRegression model = new LogisticRegression(0.01, 1000);
        model.fit(new double[][]{{1,2},{2,3},{3,4},{4,5}}, new int[]{0,0,1,1});
        System.out.println(model.predict(new double[]{2.5, 3.5})); // 1
    }
}
