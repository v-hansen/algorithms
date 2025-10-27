class LogisticRegression {
    private w: number[] = [];
    private b: number = 0;
    private lr: number;
    private maxIters: number;
    
    constructor(lr: number = 0.01, maxIters: number = 1000) {
        this.lr = lr;
        this.maxIters = maxIters;
    }
    
    private sigmoid(z: number): number {
        return 1 / (1 + Math.exp(-Math.max(-500, Math.min(500, z))));
    }
    
    fit(X: number[][], y: number[]): void {
        this.w = new Array(X[0].length).fill(0);
        this.b = 0;
        
        for (let iter = 0; iter < this.maxIters; iter++) {
            let dw = new Array(this.w.length).fill(0);
            let db = 0;
            
            for (let i = 0; i < X.length; i++) {
                let z = X[i].reduce((sum, x, j) => sum + x * this.w[j], 0) + this.b;
                let h = this.sigmoid(z);
                let error = h - y[i];
                
                for (let j = 0; j < this.w.length; j++) {
                    dw[j] += error * X[i][j];
                }
                db += error;
            }
            
            for (let j = 0; j < this.w.length; j++) {
                this.w[j] -= this.lr * dw[j] / X.length;
            }
            this.b -= this.lr * db / X.length;
        }
    }
    
    predict(X: number[][]): number[] {
        return X.map(x => {
            let z = x.reduce((sum, val, j) => sum + val * this.w[j], 0) + this.b;
            return this.sigmoid(z) >= 0.5 ? 1 : 0;
        });
    }
}

const X = [[1, 2], [2, 3], [3, 4], [4, 5]];
const y = [0, 0, 1, 1];
const model = new LogisticRegression();
model.fit(X, y);
console.log(model.predict([[2.5, 3.5]])); // [1]
