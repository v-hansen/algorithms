use rand::Rng;

struct KMeans {
    k: usize,
    max_iters: usize,
    centroids: Vec<Vec<f64>>,
}

impl KMeans {
    fn new(k: usize, max_iters: usize) -> Self {
        Self {
            k,
            max_iters,
            centroids: Vec::new(),
        }
    }
    
    fn fit(&mut self, x: &[Vec<f64>]) -> Vec<usize> {
        let mut rng = rand::thread_rng();
        
        // Initialize centroids randomly
        self.centroids = (0..self.k)
            .map(|_| x[rng.gen_range(0..x.len())].clone())
            .collect();
        
        for _ in 0..self.max_iters {
            let labels: Vec<usize> = x.iter().map(|point| {
                self.centroids.iter().enumerate()
                    .min_by(|(_, c1), (_, c2)| {
                        let d1: f64 = point.iter().zip(c1.iter())
                            .map(|(a, b)| (a - b).powi(2)).sum();
                        let d2: f64 = point.iter().zip(c2.iter())
                            .map(|(a, b)| (a - b).powi(2)).sum();
                        d1.partial_cmp(&d2).unwrap()
                    })
                    .map(|(i, _)| i)
                    .unwrap_or(0)
            }).collect();
            
            // Update centroids
            let mut new_centroids = vec![vec![0.0; x[0].len()]; self.k];
            let mut counts = vec![0; self.k];
            
            for (point, &label) in x.iter().zip(labels.iter()) {
                for (j, &val) in point.iter().enumerate() {
                    new_centroids[label][j] += val;
                }
                counts[label] += 1;
            }
            
            for i in 0..self.k {
                if counts[i] > 0 {
                    for j in 0..new_centroids[i].len() {
                        new_centroids[i][j] /= counts[i] as f64;
                    }
                }
            }
            self.centroids = new_centroids;
        }
        
        // Final assignment
        x.iter().map(|point| {
            self.centroids.iter().enumerate()
                .min_by(|(_, c1), (_, c2)| {
                    let d1: f64 = point.iter().zip(c1.iter())
                        .map(|(a, b)| (a - b).powi(2)).sum();
                    let d2: f64 = point.iter().zip(c2.iter())
                        .map(|(a, b)| (a - b).powi(2)).sum();
                    d1.partial_cmp(&d2).unwrap()
                })
                .map(|(i, _)| i)
                .unwrap_or(0)
        }).collect()
    }
}

fn main() {
    let x = vec![
        vec![1.0, 2.0], vec![1.0, 4.0], vec![1.0, 0.0],
        vec![10.0, 2.0], vec![10.0, 4.0], vec![10.0, 0.0]
    ];
    let mut kmeans = KMeans::new(2, 100);
    let labels = kmeans.fit(&x);
    println!("{:?}", labels);
}
