fn two_sum(arr: &[i32], target: i32) -> Option<(usize, usize)> {
    let (mut left, mut right) = (0, arr.len() - 1);
    while left < right {
        match arr[left] + arr[right] {
            sum if sum == target => return Some((left, right)),
            sum if sum < target => left += 1,
            _ => right -= 1,
        }
    }
    None
}

fn main() {
    let arr = [1, 2, 3, 4, 6];
    if let Some((i, j)) = two_sum(&arr, 6) {
        println!("[{}, {}]", i, j);
    }
}
