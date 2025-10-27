class SVM {
    private lr: number;
    private lambdaParam: number;
    private nIters: number;
    private w: number[] | null = null;
    private b: number = 0;
    
    constructor(lr: number = 0.001, lambdaParam: number = 0.01, nIters: number = 1000) {
        this.lr = lr;
        this.lambdaParam = lambdaParam;
        this.nIters = nIters;
    }
    
    fit(X: number[][], y: number[]): void {
        // Convert labels to -1 and 1
        const y_ = y.map(label => label <= 0 ? -1 : 1);
        
        const nFeatures = X[0].length;
        this.w = new Array(nFeatures).fill(0);
        this.b = 0;
        
        for (let iter = 0; iter < this.nIters; iter++) {
            for (let i = 0; i < X.length; i++) {
                const xi = X[i];
                const yi = y_[i];
                
                const condition = yi * (this.dotProduct(xi, this.w!) - this.b) >= 1;
                
                if (condition) {
                    for (let j = 0; j < this.w!.length; j++) {
                        this.w![j] -= this.lr * (2 * this.lambdaParam * this.w![j]);
                    }
                } else {
                    for (let j = 0; j < this.w!.length; j++) {
                        this.w![j] -= this.lr * (2 * this.lambdaParam * this.w![j] - xi[j] * yi);
                    }
                    this.b -= this.lr * yi;
                }
            }
        }
    }
    
    private dotProduct(a: number[], b: number[]): number {
        return a.reduce((sum, val, i) => sum + val * b[i], 0);
    }
    
    predict(X: number[][]): number[] {
        return X.map(x => {
            const approx = this.dotProduct(x, this.w!) - this.b;
            return Math.sign(approx);
        }).map(pred => (pred + 1) / 2); // Convert back to 0,1
    }
}

// Test
const X = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]];
const y = [0, 0, 0, 1, 1, 1];

const model = new SVM();
model.fit(X, y);
const predictions = model.predict([[2, 2], [7, 6]]);
console.log(predictions); // [0, 1]
