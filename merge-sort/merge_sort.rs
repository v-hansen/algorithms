fn merge_sort(mut arr: Vec<i32>) -> Vec<i32> {
    if arr.len() <= 1 { return arr; }
    
    let mid = arr.len() / 2;
    let right = arr.split_off(mid);
    
    merge(merge_sort(arr), merge_sort(right))
}

fn merge(left: Vec<i32>, right: Vec<i32>) -> Vec<i32> {
    let mut result = Vec::new();
    let (mut i, mut j) = (0, 0);
    
    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            result.push(left[i]);
            i += 1;
        } else {
            result.push(right[j]);
            j += 1;
        }
    }
    
    result.extend_from_slice(&left[i..]);
    result.extend_from_slice(&right[j..]);
    result
}

fn main() {
    let arr = vec![64, 34, 25, 12, 22, 11, 90];
    println!("{:?}", merge_sort(arr));
}
