public class LinearRegression {
    private double w, b;
    
    public void fit(double[] X, double[] y) {
        double X_mean = 0, y_mean = 0;
        for (int i = 0; i < X.length; i++) {
            X_mean += X[i];
            y_mean += y[i];
        }
        X_mean /= X.length;
        y_mean /= y.length;
        
        double num = 0, den = 0;
        for (int i = 0; i < X.length; i++) {
            num += (X[i] - X_mean) * (y[i] - y_mean);
            den += Math.pow(X[i] - X_mean, 2);
        }
        w = num / den;
        b = y_mean - w * X_mean;
    }
    
    public double predict(double x) {
        return w * x + b;
    }
    
    public static void main(String[] args) {
        LinearRegression model = new LinearRegression();
        model.fit(new double[]{1, 2, 3, 4, 5}, new double[]{2, 4, 6, 8, 10});
        System.out.println(model.predict(6)); // 12.0
    }
}
