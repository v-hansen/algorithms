fn binary_search(arr: &[i32], target: i32) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    while left <= right {
        let mid = left + (right - left) / 2;
        match arr[mid as usize].cmp(&target) {
            std::cmp::Ordering::Equal => return mid,
            std::cmp::Ordering::Less => left = mid + 1,
            std::cmp::Ordering::Greater => right = mid - 1,
        }
    }
    -1
}

fn main() {
    let arr = [1, 3, 5, 7, 9, 11];
    println!("{}", binary_search(&arr, 7));
    println!("{}", binary_search(&arr, 4));
}
