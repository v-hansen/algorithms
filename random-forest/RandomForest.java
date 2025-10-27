import java.util.*;

class SimpleDecisionTree {
    private int maxDepth;
    private Integer feature;
    private Double threshold;
    private Object left, right;
    
    public SimpleDecisionTree(int maxDepth) {
        this.maxDepth = maxDepth;
    }
    
    private double gini(int[] y) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int label : y) {
            counts.put(label, counts.getOrDefault(label, 0) + 1);
        }
        double impurity = 1.0;
        for (int count : counts.values()) {
            double prob = (double) count / y.length;
            impurity -= prob * prob;
        }
        return impurity;
    }
    
    public Object fit(double[][] X, int[] y, int depth) {
        if (depth >= maxDepth || Arrays.stream(y).distinct().count() == 1) {
            return Arrays.stream(y).boxed()
                .collect(Collectors.groupingBy(i -> i, Collectors.counting()))
                .entrySet().stream().max(Map.Entry.comparingByValue())
                .get().getKey();
        }
        
        double bestGini = Double.POSITIVE_INFINITY;
        Integer bestFeature = null;
        Double bestThreshold = null;
        
        // Random feature selection
        int nFeatures = (int) Math.sqrt(X[0].length);
        Random rand = new Random();
        Set<Integer> features = new HashSet<>();
        while (features.size() < nFeatures) {
            features.add(rand.nextInt(X[0].length));
        }
        
        for (int feature : features) {
            Set<Double> thresholds = new HashSet<>();
            for (double[] x : X) {
                thresholds.add(x[feature]);
            }
            
            for (double threshold : thresholds) {
                List<Integer> yLeft = new ArrayList<>();
                List<Integer> yRight = new ArrayList<>();
                
                for (int i = 0; i < X.length; i++) {
                    if (X[i][feature] <= threshold) {
                        yLeft.add(y[i]);
                    } else {
                        yRight.add(y[i]);
                    }
                }
                
                if (yLeft.isEmpty() || yRight.isEmpty()) continue;
                
                int[] yLeftArr = yLeft.stream().mapToInt(i -> i).toArray();
                int[] yRightArr = yRight.stream().mapToInt(i -> i).toArray();
                
                double gini = (yLeft.size() * gini(yLeftArr) + yRight.size() * gini(yRightArr)) / y.length;
                if (gini < bestGini) {
                    bestGini = gini;
                    bestFeature = feature;
                    bestThreshold = threshold;
                }
            }
        }
        
        if (bestFeature == null) {
            return Arrays.stream(y).boxed()
                .collect(Collectors.groupingBy(i -> i, Collectors.counting()))
                .entrySet().stream().max(Map.Entry.comparingByValue())
                .get().getKey();
        }
        
        this.feature = bestFeature;
        this.threshold = bestThreshold;
        
        // Split data
        List<double[]> XLeft = new ArrayList<>();
        List<double[]> XRight = new ArrayList<>();
        List<Integer> yLeft = new ArrayList<>();
        List<Integer> yRight = new ArrayList<>();
        
        for (int i = 0; i < X.length; i++) {
            if (X[i][bestFeature] <= bestThreshold) {
                XLeft.add(X[i]);
                yLeft.add(y[i]);
            } else {
                XRight.add(X[i]);
                yRight.add(y[i]);
            }
        }
        
        this.left = new SimpleDecisionTree(maxDepth).fit(
            XLeft.toArray(new double[0][]), yLeft.stream().mapToInt(i -> i).toArray(), depth + 1);
        this.right = new SimpleDecisionTree(maxDepth).fit(
            XRight.toArray(new double[0][]), yRight.stream().mapToInt(i -> i).toArray(), depth + 1);
        
        return this;
    }
    
    public int predictOne(double[] x) {
        if (feature == null) return (Integer) this;
        
        if (x[feature] <= threshold) {
            return left instanceof SimpleDecisionTree ? 
                ((SimpleDecisionTree) left).predictOne(x) : (Integer) left;
        } else {
            return right instanceof SimpleDecisionTree ? 
                ((SimpleDecisionTree) right).predictOne(x) : (Integer) right;
        }
    }
}

public class RandomForest {
    private int nTrees;
    private int maxDepth;
    private List<SimpleDecisionTree> trees;
    
    public RandomForest(int nTrees, int maxDepth) {
        this.nTrees = nTrees;
        this.maxDepth = maxDepth;
        this.trees = new ArrayList<>();
    }
    
    public void fit(double[][] X, int[] y) {
        trees.clear();
        Random rand = new Random();
        
        for (int i = 0; i < nTrees; i++) {
            // Bootstrap sampling
            double[][] XSample = new double[X.length][];
            int[] ySample = new int[y.length];
            
            for (int j = 0; j < X.length; j++) {
                int idx = rand.nextInt(X.length);
                XSample[j] = X[idx];
                ySample[j] = y[idx];
            }
            
            SimpleDecisionTree tree = new SimpleDecisionTree(maxDepth);
            Object result = tree.fit(XSample, ySample, 0);
            if (result instanceof SimpleDecisionTree) {
                trees.add((SimpleDecisionTree) result);
            }
        }
    }
    
    public int[] predict(double[][] X) {
        int[] predictions = new int[X.length];
        
        for (int i = 0; i < X.length; i++) {
            Map<Integer, Integer> counts = new HashMap<>();
            
            for (SimpleDecisionTree tree : trees) {
                int pred = tree.predictOne(X[i]);
                counts.put(pred, counts.getOrDefault(pred, 0) + 1);
            }
            
            predictions[i] = counts.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .get().getKey();
        }
        
        return predictions;
    }
    
    public static void main(String[] args) {
        double[][] X = {{1, 2}, {2, 3}, {3, 1}, {6, 5}, {7, 7}, {8, 6}};
        int[] y = {0, 0, 0, 1, 1, 1};
        
        RandomForest model = new RandomForest(5, 3);
        model.fit(X, y);
        int[] predictions = model.predict(new double[][]{{2, 2}, {7, 6}});
        System.out.println(Arrays.toString(predictions)); // [0, 1]
    }
}
