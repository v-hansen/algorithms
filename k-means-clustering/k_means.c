#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

typedef struct {
    double** centroids;
    int k;
    int maxIters;
    int nFeatures;
} KMeans;

KMeans* createKMeans(int k, int maxIters) {
    KMeans* kmeans = malloc(sizeof(KMeans));
    kmeans->k = k;
    kmeans->maxIters = maxIters;
    return kmeans;
}

void fit(KMeans* kmeans, double** X, int nSamples, int nFeatures) {
    kmeans->nFeatures = nFeatures;
    kmeans->centroids = malloc(kmeans->k * sizeof(double*));
    
    srand(time(NULL));
    for (int i = 0; i < kmeans->k; i++) {
        kmeans->centroids[i] = malloc(nFeatures * sizeof(double));
        int randomIdx = rand() % nSamples;
        for (int j = 0; j < nFeatures; j++) {
            kmeans->centroids[i][j] = X[randomIdx][j];
        }
    }
    
    for (int iter = 0; iter < kmeans->maxIters; iter++) {
        int* labels = malloc(nSamples * sizeof(int));
        
        for (int i = 0; i < nSamples; i++) {
            double minDist = INFINITY;
            int label = 0;
            for (int j = 0; j < kmeans->k; j++) {
                double dist = 0;
                for (int d = 0; d < nFeatures; d++) {
                    dist += pow(X[i][d] - kmeans->centroids[j][d], 2);
                }
                if (dist < minDist) {
                    minDist = dist;
                    label = j;
                }
            }
            labels[i] = label;
        }
        
        double** newCentroids = malloc(kmeans->k * sizeof(double*));
        int* counts = calloc(kmeans->k, sizeof(int));
        
        for (int i = 0; i < kmeans->k; i++) {
            newCentroids[i] = calloc(nFeatures, sizeof(double));
        }
        
        for (int i = 0; i < nSamples; i++) {
            for (int j = 0; j < nFeatures; j++) {
                newCentroids[labels[i]][j] += X[i][j];
            }
            counts[labels[i]]++;
        }
        
        for (int i = 0; i < kmeans->k; i++) {
            if (counts[i] > 0) {
                for (int j = 0; j < nFeatures; j++) {
                    newCentroids[i][j] /= counts[i];
                }
            }
        }
        
        for (int i = 0; i < kmeans->k; i++) {
            free(kmeans->centroids[i]);
            kmeans->centroids[i] = newCentroids[i];
        }
        free(newCentroids);
        free(counts);
        free(labels);
    }
}

int main() {
    double data[] = {1, 2, 1, 4, 1, 0, 10, 2, 10, 4, 10, 0};
    double* X[] = {&data[0], &data[2], &data[4], &data[6], &data[8], &data[10]};
    
    KMeans* kmeans = createKMeans(2, 100);
    fit(kmeans, X, 6, 2);
    printf("K-Means clustering completed\n");
    
    for (int i = 0; i < kmeans->k; i++) {
        free(kmeans->centroids[i]);
    }
    free(kmeans->centroids);
    free(kmeans);
}
