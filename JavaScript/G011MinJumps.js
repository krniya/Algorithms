function minJumps(arr, n) {
    //code here
    if (n <= 1) {
        return 0
    }
    if (arr[0] === 0) {
        return -1
    }
    let count = 0
    let len = 0
    while (len < n) {
        if (arr[len] === 0) {
            return -1
        }
        let val = arr[len]
        len += val
        count++
    }
    return count
}

console.log(minJumps([2, 3, 1, 1, 2, 4, 2, 0, 1, 1], 10))