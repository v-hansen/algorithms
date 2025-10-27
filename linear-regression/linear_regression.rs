struct LinearRegression {
    w: f64,
    b: f64,
}

impl LinearRegression {
    fn new() -> Self {
        Self { w: 0.0, b: 0.0 }
    }
    
    fn fit(&mut self, x: &[f64], y: &[f64]) {
        let x_mean = x.iter().sum::<f64>() / x.len() as f64;
        let y_mean = y.iter().sum::<f64>() / y.len() as f64;
        
        let mut num = 0.0;
        let mut den = 0.0;
        for i in 0..x.len() {
            num += (x[i] - x_mean) * (y[i] - y_mean);
            den += (x[i] - x_mean).powi(2);
        }
        self.w = num / den;
        self.b = y_mean - self.w * x_mean;
    }
    
    fn predict(&self, x: f64) -> f64 {
        self.w * x + self.b
    }
}

fn main() {
    let mut model = LinearRegression::new();
    model.fit(&[1.0, 2.0, 3.0, 4.0, 5.0], &[2.0, 4.0, 6.0, 8.0, 10.0]);
    println!("{}", model.predict(6.0)); // 12
}
