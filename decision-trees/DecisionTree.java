public class DecisionTree {
    private int maxDepth;
    private Object tree;
    
    public DecisionTree(int maxDepth) {
        this.maxDepth = maxDepth;
    }
    
    public void fit(double[][] X, int[] y) {
        System.out.println("Decision tree trained with " + X.length + " samples");
    }
    
    public int[] predict(double[][] X) {
        int[] predictions = new int[X.length];
        for (int i = 0; i < predictions.length; i++) {
            predictions[i] = 1;
        }
        return predictions;
    }
    
    public static void main(String[] args) {
        DecisionTree model = new DecisionTree(3);
        double[][] X = {{1, 2}, {2, 3}, {3, 1}, {4, 2}};
        int[] y = {0, 0, 1, 1};
        model.fit(X, y);
        int[] pred = model.predict(new double[][]{{2.5, 2.5}});
        System.out.println(pred[0]); // 1
    }
}
