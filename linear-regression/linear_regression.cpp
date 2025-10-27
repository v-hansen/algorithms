#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class LinearRegression {
private:
    double w, b;
    
public:
    void fit(const vector<double>& X, const vector<double>& y) {
        double X_mean = accumulate(X.begin(), X.end(), 0.0) / X.size();
        double y_mean = accumulate(y.begin(), y.end(), 0.0) / y.size();
        
        double num = 0, den = 0;
        for (size_t i = 0; i < X.size(); i++) {
            num += (X[i] - X_mean) * (y[i] - y_mean);
            den += (X[i] - X_mean) * (X[i] - X_mean);
        }
        w = num / den;
        b = y_mean - w * X_mean;
    }
    
    double predict(double x) {
        return w * x + b;
    }
};

int main() {
    LinearRegression model;
    model.fit({1, 2, 3, 4, 5}, {2, 4, 6, 8, 10});
    cout << model.predict(6) << endl; // 12
}
