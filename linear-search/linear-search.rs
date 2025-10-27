fn linear_search(arr: &[i32], target: i32) -> Option<usize> {
    for (i, &val) in arr.iter().enumerate() {
        if val == target { return Some(i); }
    }
    None
}

fn linear_search_recursive(arr: &[i32], target: i32, index: usize) -> Option<usize> {
    if index >= arr.len() { return None; }
    if arr[index] == target { return Some(index); }
    linear_search_recursive(arr, target, index + 1)
}

fn main() {
    let arr = [1, 2, 3, 4, 5];
    println!("{:?}", linear_search(&arr, 3));
    println!("{:?}", linear_search_recursive(&arr, 3, 0));
}