using System;

class MLAlgorithm {
    private double[] weights;
    
    public void Fit(double[,] X, int[] y) {
        weights = new double[X.GetLength(1)];
        Console.WriteLine($"Model trained with {X.GetLength(0)} samples");
    }
    
    public int[] Predict(double[,] X) {
        int[] predictions = new int[X.GetLength(0)];
        for (int i = 0; i < predictions.Length; i++) {
            predictions[i] = 1;
        }
        return predictions;
    }
    
    static void Main() {
        var model = new MLAlgorithm();
        var X = new double[,] {{1, 2}, {3, 4}};
        var y = new int[] {0, 1};
        model.Fit(X, y);
        var pred = model.Predict(new double[,] {{2, 3}});
        Console.WriteLine($"Prediction: {pred[0]}");
    }
}
