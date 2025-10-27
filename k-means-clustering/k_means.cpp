#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
using namespace std;

class KMeans {
private:
    int k, maxIters;
    vector<vector<double>> centroids;
    
public:
    KMeans(int k = 3, int maxIters = 100) : k(k), maxIters(maxIters) {}
    
    vector<int> fit(const vector<vector<double>>& X) {
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(0, X.size() - 1);
        
        centroids.clear();
        for (int i = 0; i < k; i++) {
            centroids.push_back(X[dis(gen)]);
        }
        
        for (int iter = 0; iter < maxIters; iter++) {
            vector<int> labels(X.size());
            
            for (size_t i = 0; i < X.size(); i++) {
                double minDist = INFINITY;
                int label = 0;
                for (int j = 0; j < k; j++) {
                    double dist = 0;
                    for (size_t d = 0; d < X[i].size(); d++) {
                        dist += pow(X[i][d] - centroids[j][d], 2);
                    }
                    dist = sqrt(dist);
                    if (dist < minDist) {
                        minDist = dist;
                        label = j;
                    }
                }
                labels[i] = label;
            }
            
            vector<vector<double>> newCentroids(k, vector<double>(X[0].size(), 0));
            vector<int> counts(k, 0);
            
            for (size_t i = 0; i < X.size(); i++) {
                for (size_t j = 0; j < X[i].size(); j++) {
                    newCentroids[labels[i]][j] += X[i][j];
                }
                counts[labels[i]]++;
            }
            
            for (int i = 0; i < k; i++) {
                if (counts[i] > 0) {
                    for (size_t j = 0; j < newCentroids[i].size(); j++) {
                        newCentroids[i][j] /= counts[i];
                    }
                }
            }
            centroids = newCentroids;
        }
        
        vector<int> labels(X.size());
        for (size_t i = 0; i < X.size(); i++) {
            double minDist = INFINITY;
            int label = 0;
            for (int j = 0; j < k; j++) {
                double dist = 0;
                for (size_t d = 0; d < X[i].size(); d++) {
                    dist += pow(X[i][d] - centroids[j][d], 2);
                }
                if (dist < minDist) {
                    minDist = dist;
                    label = j;
                }
            }
            labels[i] = label;
        }
        return labels;
    }
};

int main() {
    KMeans kmeans(2);
    vector<vector<double>> X = {{1, 2}, {1, 4}, {1, 0}, {10, 2}, {10, 4}, {10, 0}};
    auto labels = kmeans.fit(X);
    for (int label : labels) cout << label << " ";
    cout << endl;
}
