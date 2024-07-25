var sortArray = function (nums) {
    mergeSort(nums, 0, nums.length - 1);
    return nums;
};

function mergeSort(array, low, high) {
    if (low >= high) return;

    const mid = Math.floor((low + high) / 2);
    mergeSort(array, low, mid);
    mergeSort(array, mid + 1, high);
    merge(array, low, mid, high);
}

function merge(array, low, mid, high) {
    const n1 = mid - low + 1;
    const n2 = high - mid;
    const leftPart = array.slice(low, mid + 1);
    const rightPart = array.slice(mid + 1, high + 1);

    let p1 = 0,
        p2 = 0,
        writeInd = low;

    while (p1 < n1 && p2 < n2) {
        if (leftPart[p1] <= rightPart[p2]) {
            array[writeInd++] = leftPart[p1++];
        } else {
            array[writeInd++] = rightPart[p2++];
        }
    }

    while (p1 < n1) {
        array[writeInd++] = leftPart[p1++];
    }

    while (p2 < n2) {
        array[writeInd++] = rightPart[p2++];
    }
}
