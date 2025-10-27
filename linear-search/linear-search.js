function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

const arr = [5, 2, 8, 1, 9, 3];
console.log(linearSearch(arr, 8));
console.log(linearSearch(arr, 7));
