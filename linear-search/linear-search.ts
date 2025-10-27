function linearSearch(arr: number[], target: number): number {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

function linearSearchRecursive(arr: number[], target: number, index: number = 0): number {
    if (index >= arr.length) return -1;
    if (arr[index] === target) return index;
    return linearSearchRecursive(arr, target, index + 1);
}

console.log(linearSearch([1, 2, 3, 4, 5], 3));
console.log(linearSearchRecursive([1, 2, 3, 4, 5], 3));