function twoSum(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left < right) {
        const sum = arr[left] + arr[right];
        if (sum === target) return [left, right];
        sum < target ? left++ : right--;
    }
    return [];
}

console.log(twoSum([1, 2, 3, 4, 6], 6)); // [1, 3]
