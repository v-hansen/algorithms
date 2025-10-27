#include <stdio.h>

typedef struct {
    double w, b;
} LinearRegression;

void fit(LinearRegression* model, double* X, double* y, int n) {
    double X_mean = 0, y_mean = 0;
    for (int i = 0; i < n; i++) {
        X_mean += X[i];
        y_mean += y[i];
    }
    X_mean /= n;
    y_mean /= n;
    
    double num = 0, den = 0;
    for (int i = 0; i < n; i++) {
        num += (X[i] - X_mean) * (y[i] - y_mean);
        den += (X[i] - X_mean) * (X[i] - X_mean);
    }
    model->w = num / den;
    model->b = y_mean - model->w * X_mean;
}

double predict(LinearRegression* model, double x) {
    return model->w * x + model->b;
}

int main() {
    LinearRegression model;
    double X[] = {1, 2, 3, 4, 5};
    double y[] = {2, 4, 6, 8, 10};
    fit(&model, X, y, 5);
    printf("%.1f\n", predict(&model, 6)); // 12.0
}
