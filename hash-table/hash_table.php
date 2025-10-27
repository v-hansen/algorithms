<?php
class HashTable {
    private $buckets;
    private $size;
    
    public function __construct($size = 10) {
        $this->size = $size;
        $this->buckets = array_fill(0, $size, []);
    }
    
    private function hash($key) {
        $sum = 0;
        for ($i = 0; $i < strlen($key); $i++) {
            $sum += ord($key[$i]);
        }
        return $sum % $this->size;
    }
    
    public function put($key, $value) {
        $index = $this->hash($key);
        
        foreach ($this->buckets[$index] as &$pair) {
            if ($pair['key'] === $key) {
                $pair['value'] = $value;
                return;
            }
        }
        
        $this->buckets[$index][] = ['key' => $key, 'value' => $value];
    }
    
    public function get($key) {
        $index = $this->hash($key);
        
        foreach ($this->buckets[$index] as $pair) {
            if ($pair['key'] === $key) {
                return $pair['value'];
            }
        }
        
        return null;
    }
}

$ht = new HashTable();
$ht->put("key1", 100);
echo $ht->get("key1");
?>