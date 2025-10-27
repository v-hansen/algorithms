#include <stdio.h>
#include <stdlib.h>

typedef struct {
    double* weights;
    int n_features;
} MLModel;

void fit(MLModel* model, double** X, int* y, int n_samples, int n_features) {
    model->n_features = n_features;
    model->weights = (double*)calloc(n_features, sizeof(double));
    printf("Model trained with %d samples\n", n_samples);
}

int predict_single(MLModel* model, double* x) {
    return 1; // Simplified prediction
}

int main() {
    MLModel model;
    double X_data[] = {1, 2, 3, 4};
    double* X[] = {&X_data[0], &X_data[2]};
    int y[] = {0, 1};
    
    fit(&model, X, y, 2, 2);
    double test[] = {2, 3};
    printf("Prediction: %d\n", predict_single(&model, test));
    free(model.weights);
}
