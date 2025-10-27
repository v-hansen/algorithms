class KNN {
    private k: number;
    private X_train: number[][] = [];
    private y_train: number[] = [];
    
    constructor(k: number = 3) {
        this.k = k;
    }
    
    fit(X: number[][], y: number[]): void {
        this.X_train = X;
        this.y_train = y;
    }
    
    private euclideanDistance(x1: number[], x2: number[]): number {
        return Math.sqrt(x1.reduce((sum, val, i) => sum + Math.pow(val - x2[i], 2), 0));
    }
    
    predict(X: number[][]): number[] {
        return X.map(x => {
            const distances = this.X_train.map((x_train, i) => ({
                distance: this.euclideanDistance(x, x_train),
                label: this.y_train[i]
            }));
            
            distances.sort((a, b) => a.distance - b.distance);
            const kNearest = distances.slice(0, this.k);
            
            const counts: {[key: number]: number} = {};
            kNearest.forEach(item => {
                counts[item.label] = (counts[item.label] || 0) + 1;
            });
            
            return parseInt(Object.keys(counts).reduce((a, b) => counts[parseInt(a)] > counts[parseInt(b)] ? a : b));
        });
    }
}

const X_train = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]];
const y_train = [0, 0, 0, 1, 1, 1];
const X_test = [[2, 2], [7, 6]];

const model = new KNN(3);
model.fit(X_train, y_train);
console.log(model.predict(X_test)); // [0, 1]
