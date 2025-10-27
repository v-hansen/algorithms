package main

import "fmt"

type LinearRegression struct {
    w, b float64
}

func (lr *LinearRegression) Fit(X, y []float64) {
    var X_mean, y_mean float64
    for i := range X {
        X_mean += X[i]
        y_mean += y[i]
    }
    X_mean /= float64(len(X))
    y_mean /= float64(len(y))
    
    var num, den float64
    for i := range X {
        num += (X[i] - X_mean) * (y[i] - y_mean)
        den += (X[i] - X_mean) * (X[i] - X_mean)
    }
    lr.w = num / den
    lr.b = y_mean - lr.w*X_mean
}

func (lr *LinearRegression) Predict(x float64) float64 {
    return lr.w*x + lr.b
}

func main() {
    model := &LinearRegression{}
    model.Fit([]float64{1, 2, 3, 4, 5}, []float64{2, 4, 6, 8, 10})
    fmt.Println(model.Predict(6)) // 12
}
