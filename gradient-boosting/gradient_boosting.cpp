#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class MLAlgorithm {
public:
    void fit(const vector<vector<double>>& X, const vector<int>& y) {
        // Simplified implementation
        cout << "Model trained with " << X.size() << " samples" << endl;
    }
    
    vector<int> predict(const vector<vector<double>>& X) {
        vector<int> predictions(X.size(), 1);
        return predictions;
    }
};

int main() {
    MLAlgorithm model;
    vector<vector<double>> X = {{1, 2}, {3, 4}};
    vector<int> y = {0, 1};
    model.fit(X, y);
    auto pred = model.predict({{2, 3}});
    cout << "Prediction: " << pred[0] << endl;
}
