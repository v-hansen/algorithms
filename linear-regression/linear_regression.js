class LinearRegression {
    constructor() {
        this.w = null;
        this.b = null;
    }
    
    fit(X, y) {
        const X_mean = X.reduce((a, b) => a + b) / X.length;
        const y_mean = y.reduce((a, b) => a + b) / y.length;
        
        let num = 0, den = 0;
        for (let i = 0; i < X.length; i++) {
            num += (X[i] - X_mean) * (y[i] - y_mean);
            den += (X[i] - X_mean) ** 2;
        }
        this.w = num / den;
        this.b = y_mean - this.w * X_mean;
    }
    
    predict(X) {
        return X.map(x => this.w * x + this.b);
    }
}

const X = [1, 2, 3, 4, 5];
const y = [2, 4, 6, 8, 10];
const model = new LinearRegression();
model.fit(X, y);
console.log(model.predict([6])); // [12]
