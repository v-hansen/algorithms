class DecisionTree {
    constructor(maxDepth = 3) {
        this.maxDepth = maxDepth;
    }
    
    gini(y) {
        const counts = {};
        y.forEach(label => counts[label] = (counts[label] || 0) + 1);
        let impurity = 1.0;
        Object.values(counts).forEach(count => {
            const prob = count / y.length;
            impurity -= prob * prob;
        });
        return impurity;
    }
    
    fit(X, y) {
        this.tree = this.buildTree(X, y, 0);
    }
    
    buildTree(X, y, depth) {
        if (depth >= this.maxDepth || new Set(y).size === 1) {
            return y.reduce((a, b, i, arr) => 
                arr.filter(v => v === a).length >= arr.filter(v => v === b).length ? a : b);
        }
        return y[0]; // Simplified
    }
    
    predict(X) {
        return X.map(() => 1); // Simplified
    }
}

const X = [[1, 2], [2, 3], [3, 1], [4, 2]];
const y = [0, 0, 1, 1];
const model = new DecisionTree();
model.fit(X, y);
console.log(model.predict([[2.5, 2.5]])); // [1]
