fn quick_sort(arr: &mut [i32]) {
    if arr.len() <= 1 { return; }
    
    let pivot_index = partition(arr);
    let (left, right) = arr.split_at_mut(pivot_index);
    
    quick_sort(left);
    quick_sort(&mut right[1..]);
}

fn partition(arr: &mut [i32]) -> usize {
    let pivot = arr.len() - 1;
    let mut i = 0;
    
    for j in 0..pivot {
        if arr[j] <= arr[pivot] {
            arr.swap(i, j);
            i += 1;
        }
    }
    arr.swap(i, pivot);
    i
}

fn main() {
    let mut arr = [64, 34, 25, 12, 22, 11, 90];
    quick_sort(&mut arr);
    println!("{:?}", arr);
}
