class KMeans {
    private k: number;
    private maxIters: number;
    private centroids: number[][] = [];
    
    constructor(k: number = 3, maxIters: number = 100) {
        this.k = k;
        this.maxIters = maxIters;
    }
    
    fit(X: number[][]): number[] {
        // Initialize centroids randomly
        this.centroids = [];
        for (let i = 0; i < this.k; i++) {
            this.centroids.push([...X[Math.floor(Math.random() * X.length)]]);
        }
        
        for (let iter = 0; iter < this.maxIters; iter++) {
            const labels = X.map(point => {
                let minDist = Infinity;
                let label = 0;
                for (let i = 0; i < this.k; i++) {
                    const dist = Math.sqrt(point.reduce((sum, val, j) => 
                        sum + Math.pow(val - this.centroids[i][j], 2), 0));
                    if (dist < minDist) {
                        minDist = dist;
                        label = i;
                    }
                }
                return label;
            });
            
            // Update centroids
            const newCentroids: number[][] = [];
            for (let i = 0; i < this.k; i++) {
                const cluster = X.filter((_, idx) => labels[idx] === i);
                if (cluster.length > 0) {
                    newCentroids[i] = cluster[0].map((_, j) => 
                        cluster.reduce((sum, point) => sum + point[j], 0) / cluster.length);
                } else {
                    newCentroids[i] = this.centroids[i];
                }
            }
            this.centroids = newCentroids;
        }
        
        return X.map(point => {
            let minDist = Infinity;
            let label = 0;
            for (let i = 0; i < this.k; i++) {
                const dist = Math.sqrt(point.reduce((sum, val, j) => 
                    sum + Math.pow(val - this.centroids[i][j], 2), 0));
                if (dist < minDist) {
                    minDist = dist;
                    label = i;
                }
            }
            return label;
        });
    }
}

const X = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]];
const kmeans = new KMeans(2);
console.log(kmeans.fit(X));
