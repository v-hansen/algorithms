class SimpleDecisionTree {
    private maxDepth: number;
    private feature?: number;
    private threshold?: number;
    private left?: SimpleDecisionTree | number;
    private right?: SimpleDecisionTree | number;
    
    constructor(maxDepth: number = 3) {
        this.maxDepth = maxDepth;
    }
    
    private gini(y: number[]): number {
        const counts: {[key: number]: number} = {};
        y.forEach(label => counts[label] = (counts[label] || 0) + 1);
        let impurity = 1.0;
        Object.values(counts).forEach(count => {
            const prob = count / y.length;
            impurity -= prob * prob;
        });
        return impurity;
    }
    
    fit(X: number[][], y: number[], depth: number = 0): SimpleDecisionTree | number {
        if (depth >= this.maxDepth || new Set(y).size === 1) {
            return y.reduce((a, b, i, arr) => 
                arr.filter(v => v === a).length >= arr.filter(v => v === b).length ? a : b);
        }
        
        let bestGini = Infinity;
        let bestFeature: number | null = null;
        let bestThreshold: number | null = null;
        
        // Random feature selection
        const nFeatures = Math.floor(Math.sqrt(X[0].length));
        const features: number[] = [];
        while (features.length < nFeatures) {
            const f = Math.floor(Math.random() * X[0].length);
            if (!features.includes(f)) features.push(f);
        }
        
        for (const feature of features) {
            const thresholds = [...new Set(X.map(x => x[feature]))];
            for (const threshold of thresholds) {
                const leftMask = X.map(x => x[feature] <= threshold);
                const yLeft = y.filter((_, i) => leftMask[i]);
                const yRight = y.filter((_, i) => !leftMask[i]);
                
                if (yLeft.length === 0 || yRight.length === 0) continue;
                
                const gini = (yLeft.length * this.gini(yLeft) + yRight.length * this.gini(yRight)) / y.length;
                if (gini < bestGini) {
                    bestGini = gini;
                    bestFeature = feature;
                    bestThreshold = threshold;
                }
            }
        }
        
        if (bestFeature === null) {
            return y.reduce((a, b, i, arr) => 
                arr.filter(v => v === a).length >= arr.filter(v => v === b).length ? a : b);
        }
        
        const leftMask = X.map(x => x[bestFeature!] <= bestThreshold!);
        const XLeft = X.filter((_, i) => leftMask[i]);
        const XRight = X.filter((_, i) => !leftMask[i]);
        const yLeft = y.filter((_, i) => leftMask[i]);
        const yRight = y.filter((_, i) => !leftMask[i]);
        
        this.feature = bestFeature;
        this.threshold = bestThreshold;
        this.left = new SimpleDecisionTree(this.maxDepth).fit(XLeft, yLeft, depth + 1);
        this.right = new SimpleDecisionTree(this.maxDepth).fit(XRight, yRight, depth + 1);
        return this;
    }
    
    predictOne(x: number[]): number {
        if (this.feature === undefined) return this as any;
        
        if (x[this.feature] <= this.threshold!) {
            return typeof this.left === 'object' ? this.left.predictOne(x) : this.left!;
        } else {
            return typeof this.right === 'object' ? this.right.predictOne(x) : this.right!;
        }
    }
}

class RandomForest {
    private nTrees: number;
    private maxDepth: number;
    private trees: SimpleDecisionTree[] = [];
    
    constructor(nTrees: number = 10, maxDepth: number = 3) {
        this.nTrees = nTrees;
        this.maxDepth = maxDepth;
    }
    
    fit(X: number[][], y: number[]): void {
        this.trees = [];
        for (let i = 0; i < this.nTrees; i++) {
            // Bootstrap sampling
            const indices = Array.from({length: X.length}, () => Math.floor(Math.random() * X.length));
            const XSample = indices.map(i => X[i]);
            const ySample = indices.map(i => y[i]);
            
            const tree = new SimpleDecisionTree(this.maxDepth);
            const result = tree.fit(XSample, ySample);
            if (typeof result === 'object') {
                this.trees.push(result);
            }
        }
    }
    
    predict(X: number[][]): number[] {
        return X.map(x => {
            const treePredictions = this.trees.map(tree => tree.predictOne(x));
            const counts: {[key: number]: number} = {};
            treePredictions.forEach(pred => counts[pred] = (counts[pred] || 0) + 1);
            return parseInt(Object.keys(counts).reduce((a, b) => counts[parseInt(a)] > counts[parseInt(b)] ? a : b));
        });
    }
}

// Test
const X = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]];
const y = [0, 0, 0, 1, 1, 1];

const model = new RandomForest(5);
model.fit(X, y);
console.log(model.predict([[2, 2], [7, 6]])); // [0, 1]
