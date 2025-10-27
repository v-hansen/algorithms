using System;
using System.Linq;

class LinearRegression {
    private double w, b;
    
    public void Fit(double[] X, double[] y) {
        double X_mean = X.Average();
        double y_mean = y.Average();
        
        double num = 0, den = 0;
        for (int i = 0; i < X.Length; i++) {
            num += (X[i] - X_mean) * (y[i] - y_mean);
            den += Math.Pow(X[i] - X_mean, 2);
        }
        w = num / den;
        b = y_mean - w * X_mean;
    }
    
    public double Predict(double x) {
        return w * x + b;
    }
    
    static void Main() {
        var model = new LinearRegression();
        model.Fit(new double[] {1, 2, 3, 4, 5}, new double[] {2, 4, 6, 8, 10});
        Console.WriteLine(model.Predict(6)); // 12
    }
}
