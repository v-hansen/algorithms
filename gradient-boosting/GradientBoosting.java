import java.util.*;

class Tree {
    Double prediction;
    Integer feature;
    Double threshold;
    Double leftPred;
    Double rightPred;
    
    Tree(double prediction) {
        this.prediction = prediction;
    }
    
    Tree(int feature, double threshold, double leftPred, double rightPred) {
        this.feature = feature;
        this.threshold = threshold;
        this.leftPred = leftPred;
        this.rightPred = rightPred;
    }
}

public class GradientBoosting {
    private int nEstimators;
    private double learningRate;
    private int maxDepth;
    private List<Tree> trees;
    private double initialPrediction;
    
    public GradientBoosting(int nEstimators, double learningRate, int maxDepth) {
        this.nEstimators = nEstimators;
        this.learningRate = learningRate;
        this.maxDepth = maxDepth;
        this.trees = new ArrayList<>();
    }
    
    public GradientBoosting() {
        this(10, 0.1, 3);
    }
    
    private double sigmoid(double x) {
        return 1.0 / (1.0 + Math.exp(-Math.max(-500, Math.min(500, x))));
    }
    
    public void fit(double[][] X, int[] y) {
        // Initialize with log odds
        double meanY = Arrays.stream(y).average().orElse(0.5);
        initialPrediction = Math.log(meanY / (1 - meanY));
        
        // Current predictions
        double[] currentPredictions = new double[y.length];
        Arrays.fill(currentPredictions, initialPrediction);
        
        for (int i = 0; i < nEstimators; i++) {
            // Calculate residuals (negative gradient)
            double[] probabilities = new double[currentPredictions.length];
            for (int j = 0; j < currentPredictions.length; j++) {
                probabilities[j] = sigmoid(currentPredictions[j]);
            }
            
            double[] residuals = new double[y.length];
            for (int j = 0; j < y.length; j++) {
                residuals[j] = y[j] - probabilities[j];
            }
            
            // Fit a simple regression tree to residuals
            Tree tree = fitTree(X, residuals);
            trees.add(tree);
            
            // Update predictions
            double[] treePredictions = predictTree(X, tree);
            for (int j = 0; j < currentPredictions.length; j++) {
                currentPredictions[j] += learningRate * treePredictions[j];
            }
        }
    }
    
    private Tree fitTree(double[][] X, double[] y) {
        double bestMse = Double.POSITIVE_INFINITY;
        Integer bestFeature = null;
        Double bestThreshold = null;
        
        for (int feature = 0; feature < X[0].length; feature++) {
            Set<Double> thresholds = new HashSet<>();
            for (double[] x : X) {
                thresholds.add(x[feature]);
            }
            
            for (double threshold : thresholds) {
                List<Double> yLeft = new ArrayList<>();
                List<Double> yRight = new ArrayList<>();
                
                for (int i = 0; i < X.length; i++) {
                    if (X[i][feature] <= threshold) {
                        yLeft.add(y[i]);
                    } else {
                        yRight.add(y[i]);
                    }
                }
                
                if (yLeft.isEmpty() || yRight.isEmpty()) continue;
                
                double leftPred = yLeft.stream().mapToDouble(Double::doubleValue).average().orElse(0);
                double rightPred = yRight.stream().mapToDouble(Double::doubleValue).average().orElse(0);
                
                double mse = yLeft.stream().mapToDouble(yi -> Math.pow(yi - leftPred, 2)).sum() +
                            yRight.stream().mapToDouble(yi -> Math.pow(yi - rightPred, 2)).sum();
                
                if (mse < bestMse) {
                    bestMse = mse;
                    bestFeature = feature;
                    bestThreshold = threshold;
                }
            }
        }
        
        if (bestFeature == null) {
            double prediction = Arrays.stream(y).average().orElse(0);
            return new Tree(prediction);
        }
        
        List<Double> yLeft = new ArrayList<>();
        List<Double> yRight = new ArrayList<>();
        
        for (int i = 0; i < X.length; i++) {
            if (X[i][bestFeature] <= bestThreshold) {
                yLeft.add(y[i]);
            } else {
                yRight.add(y[i]);
            }
        }
        
        double leftPred = yLeft.isEmpty() ? 0 : yLeft.stream().mapToDouble(Double::doubleValue).average().orElse(0);
        double rightPred = yRight.isEmpty() ? 0 : yRight.stream().mapToDouble(Double::doubleValue).average().orElse(0);
        
        return new Tree(bestFeature, bestThreshold, leftPred, rightPred);
    }
    
    private double[] predictTree(double[][] X, Tree tree) {
        double[] predictions = new double[X.length];
        
        if (tree.prediction != null) {
            Arrays.fill(predictions, tree.prediction);
            return predictions;
        }
        
        for (int i = 0; i < X.length; i++) {
            predictions[i] = X[i][tree.feature] <= tree.threshold ? tree.leftPred : tree.rightPred;
        }
        
        return predictions;
    }
    
    public int[] predict(double[][] X) {
        double[] predictions = new double[X.length];
        Arrays.fill(predictions, initialPrediction);
        
        for (Tree tree : trees) {
            double[] treePredictions = predictTree(X, tree);
            for (int i = 0; i < predictions.length; i++) {
                predictions[i] += learningRate * treePredictions[i];
            }
        }
        
        int[] result = new int[X.length];
        for (int i = 0; i < predictions.length; i++) {
            double probability = sigmoid(predictions[i]);
            result[i] = probability >= 0.5 ? 1 : 0;
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        double[][] X = {{1, 2}, {2, 3}, {3, 1}, {6, 5}, {7, 7}, {8, 6}};
        int[] y = {0, 0, 0, 1, 1, 1};
        
        GradientBoosting model = new GradientBoosting(5, 0.1, 3);
        model.fit(X, y);
        int[] predictions = model.predict(new double[][]{{2, 2}, {7, 6}});
        System.out.println(Arrays.toString(predictions)); // [0, 1]
    }
}
