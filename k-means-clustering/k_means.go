package main

import (
    "fmt"
    "math"
    "math/rand"
    "time"
)

type KMeans struct {
    k         int
    maxIters  int
    centroids [][]float64
}

func NewKMeans(k, maxIters int) *KMeans {
    return &KMeans{k: k, maxIters: maxIters}
}

func (km *KMeans) Fit(X [][]float64) []int {
    rand.Seed(time.Now().UnixNano())
    
    // Initialize centroids randomly
    km.centroids = make([][]float64, km.k)
    for i := 0; i < km.k; i++ {
        randomIdx := rand.Intn(len(X))
        km.centroids[i] = make([]float64, len(X[0]))
        copy(km.centroids[i], X[randomIdx])
    }
    
    for iter := 0; iter < km.maxIters; iter++ {
        labels := make([]int, len(X))
        
        // Assign points to closest centroid
        for i, point := range X {
            minDist := math.Inf(1)
            label := 0
            for j, centroid := range km.centroids {
                dist := 0.0
                for d := range point {
                    dist += math.Pow(point[d]-centroid[d], 2)
                }
                if dist < minDist {
                    minDist = dist
                    label = j
                }
            }
            labels[i] = label
        }
        
        // Update centroids
        newCentroids := make([][]float64, km.k)
        counts := make([]int, km.k)
        
        for i := 0; i < km.k; i++ {
            newCentroids[i] = make([]float64, len(X[0]))
        }
        
        for i, point := range X {
            for j, val := range point {
                newCentroids[labels[i]][j] += val
            }
            counts[labels[i]]++
        }
        
        for i := 0; i < km.k; i++ {
            if counts[i] > 0 {
                for j := range newCentroids[i] {
                    newCentroids[i][j] /= float64(counts[i])
                }
            }
        }
        km.centroids = newCentroids
    }
    
    // Final assignment
    labels := make([]int, len(X))
    for i, point := range X {
        minDist := math.Inf(1)
        label := 0
        for j, centroid := range km.centroids {
            dist := 0.0
            for d := range point {
                dist += math.Pow(point[d]-centroid[d], 2)
            }
            if dist < minDist {
                minDist = dist
                label = j
            }
        }
        labels[i] = label
    }
    return labels
}

func main() {
    X := [][]float64{{1, 2}, {1, 4}, {1, 0}, {10, 2}, {10, 4}, {10, 0}}
    kmeans := NewKMeans(2, 100)
    labels := kmeans.Fit(X)
    fmt.Println(labels)
}
