class KMeans
  def initialize(k = 3, max_iters = 100)
    @k = k
    @max_iters = max_iters
  end
  
  def fit(x)
    n_samples = x.size
    n_features = x[0].size
    
    # Initialize centroids randomly
    @centroids = []
    @k.times do
      random_idx = rand(n_samples)
      @centroids << x[random_idx].dup
    end
    
    @max_iters.times do
      labels = []
      
      # Assign points to closest centroid
      x.each do |point|
        min_dist = Float::INFINITY
        label = 0
        @centroids.each_with_index do |centroid, j|
          dist = 0
          point.each_with_index do |val, d|
            dist += (val - centroid[d]) ** 2
          end
          if dist < min_dist
            min_dist = dist
            label = j
          end
        end
        labels << label
      end
      
      # Update centroids
      new_centroids = Array.new(@k) { Array.new(n_features, 0.0) }
      counts = Array.new(@k, 0)
      
      x.each_with_index do |point, i|
        point.each_with_index do |val, j|
          new_centroids[labels[i]][j] += val
        end
        counts[labels[i]] += 1
      end
      
      @k.times do |i|
        if counts[i] > 0
          n_features.times do |j|
            new_centroids[i][j] /= counts[i]
          end
        end
      end
      @centroids = new_centroids
    end
    
    # Final assignment
    final_labels = []
    x.each do |point|
      min_dist = Float::INFINITY
      label = 0
      @centroids.each_with_index do |centroid, j|
        dist = 0
        point.each_with_index do |val, d|
          dist += (val - centroid[d]) ** 2
        end
        if dist < min_dist
          min_dist = dist
          label = j
        end
      end
      final_labels << label
    end
    final_labels
  end
end

x = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]
kmeans = KMeans.new(2)
labels = kmeans.fit(x)
puts labels.join(" ")
