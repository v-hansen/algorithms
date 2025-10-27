fn linear_search(arr: &[i32], target: i32) -> i32 {
    for (i, &val) in arr.iter().enumerate() {
        if val == target {
            return i as i32;
        }
    }
    -1
}

fn main() {
    let arr = [5, 2, 8, 1, 9, 3];
    println!("{}", linear_search(&arr, 8));
    println!("{}", linear_search(&arr, 7));
}
