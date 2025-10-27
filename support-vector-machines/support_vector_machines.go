package main

import "fmt"

type MLAlgorithm struct {
    weights []float64
}

func (m *MLAlgorithm) Fit(X [][]float64, y []int) {
    m.weights = make([]float64, len(X[0]))
    fmt.Printf("Model trained with %d samples\n", len(X))
}

func (m *MLAlgorithm) Predict(X [][]float64) []int {
    predictions := make([]int, len(X))
    for i := range predictions {
        predictions[i] = 1
    }
    return predictions
}

func main() {
    model := &MLAlgorithm{}
    X := [][]float64{{1, 2}, {3, 4}}
    y := []int{0, 1}
    model.Fit(X, y)
    pred := model.Predict([][]float64{{2, 3}})
    fmt.Printf("Prediction: %d\n", pred[0])
}
