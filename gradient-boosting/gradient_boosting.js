class GradientBoosting {
    constructor(nEstimators = 10, learningRate = 0.1, maxDepth = 3) {
        this.nEstimators = nEstimators;
        this.learningRate = learningRate;
        this.maxDepth = maxDepth;
        this.trees = [];
        this.initialPrediction = 0;
    }
    
    sigmoid(x) {
        return 1 / (1 + Math.exp(-Math.max(-500, Math.min(500, x))));
    }
    
    fit(X, y) {
        // Initialize with log odds
        const meanY = y.reduce((a, b) => a + b) / y.length;
        this.initialPrediction = Math.log(meanY / (1 - meanY));
        
        // Current predictions
        let currentPredictions = new Array(y.length).fill(this.initialPrediction);
        
        for (let i = 0; i < this.nEstimators; i++) {
            // Calculate residuals (negative gradient)
            const probabilities = currentPredictions.map(p => this.sigmoid(p));
            const residuals = y.map((yi, idx) => yi - probabilities[idx]);
            
            // Fit a simple regression tree to residuals
            const tree = this.fitTree(X, residuals);
            this.trees.push(tree);
            
            // Update predictions
            const treePredictions = this.predictTree(X, tree);
            for (let j = 0; j < currentPredictions.length; j++) {
                currentPredictions[j] += this.learningRate * treePredictions[j];
            }
        }
    }
    
    fitTree(X, y) {
        let bestMse = Infinity;
        let bestFeature = null, bestThreshold = null;
        
        for (let feature = 0; feature < X[0].length; feature++) {
            const thresholds = [...new Set(X.map(x => x[feature]))];
            for (const threshold of thresholds) {
                const leftMask = X.map(x => x[feature] <= threshold);
                const yLeft = y.filter((_, i) => leftMask[i]);
                const yRight = y.filter((_, i) => !leftMask[i]);
                
                if (yLeft.length === 0 || yRight.length === 0) continue;
                
                const leftPred = yLeft.reduce((a, b) => a + b) / yLeft.length;
                const rightPred = yRight.reduce((a, b) => a + b) / yRight.length;
                
                const mse = yLeft.reduce((sum, yi) => sum + Math.pow(yi - leftPred, 2), 0) +
                           yRight.reduce((sum, yi) => sum + Math.pow(yi - rightPred, 2), 0);
                
                if (mse < bestMse) {
                    bestMse = mse;
                    bestFeature = feature;
                    bestThreshold = threshold;
                }
            }
        }
        
        if (bestFeature === null) {
            return { prediction: y.reduce((a, b) => a + b) / y.length };
        }
        
        const leftMask = X.map(x => x[bestFeature] <= bestThreshold);
        const yLeft = y.filter((_, i) => leftMask[i]);
        const yRight = y.filter((_, i) => !leftMask[i]);
        
        const leftPred = yLeft.length > 0 ? yLeft.reduce((a, b) => a + b) / yLeft.length : 0;
        const rightPred = yRight.length > 0 ? yRight.reduce((a, b) => a + b) / yRight.length : 0;
        
        return {
            feature: bestFeature,
            threshold: bestThreshold,
            leftPred: leftPred,
            rightPred: rightPred
        };
    }
    
    predictTree(X, tree) {
        if (tree.prediction !== undefined) {
            return new Array(X.length).fill(tree.prediction);
        }
        
        return X.map(x => {
            return x[tree.feature] <= tree.threshold ? tree.leftPred : tree.rightPred;
        });
    }
    
    predict(X) {
        let predictions = new Array(X.length).fill(this.initialPrediction);
        
        for (const tree of this.trees) {
            const treePredictions = this.predictTree(X, tree);
            for (let i = 0; i < predictions.length; i++) {
                predictions[i] += this.learningRate * treePredictions[i];
            }
        }
        
        const probabilities = predictions.map(p => this.sigmoid(p));
        return probabilities.map(p => p >= 0.5 ? 1 : 0);
    }
}

// Test
const X = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]];
const y = [0, 0, 0, 1, 1, 1];

const model = new GradientBoosting(5);
model.fit(X, y);
console.log(model.predict([[2, 2], [7, 6]])); // [0, 1]
