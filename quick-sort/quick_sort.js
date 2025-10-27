function quickSort(arr) {
    if (arr.length <= 1) return arr;
    
    const pivot = arr[Math.floor(arr.length / 2)];
    const left = arr.filter(x => x < pivot);
    const middle = arr.filter(x => x === pivot);
    const right = arr.filter(x => x > pivot);
    
    return [...quickSort(left), ...middle, ...quickSort(right)];
}

const arr = [64, 34, 25, 12, 22, 11, 90];
console.log(quickSort(arr)); // [11, 12, 22, 25, 34, 64, 90]
