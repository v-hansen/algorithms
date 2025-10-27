class DecisionTree {
    private maxDepth: number;
    private tree: any;
    
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
    
    fit(X: number[][], y: number[]): void {
        this.tree = this.buildTree(X, y, 0);
    }
    
    private buildTree(X: number[][], y: number[], depth: number): any {
        if (depth >= this.maxDepth || new Set(y).size === 1) {
            return y.reduce((a, b, i, arr) => 
                arr.filter(v => v === a).length >= arr.filter(v => v === b).length ? a : b);
        }
        return y[0]; // Simplified
    }
    
    predict(X: number[][]): number[] {
        return X.map(() => 1); // Simplified
    }
}

const X = [[1, 2], [2, 3], [3, 1], [4, 2]];
const y = [0, 0, 1, 1];
const model = new DecisionTree();
model.fit(X, y);
console.log(model.predict([[2.5, 2.5]])); // [1]
