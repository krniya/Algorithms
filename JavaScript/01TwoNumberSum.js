// O(n) | O(n)
function twonumbersum(array, tar) {
    const nums = {};
    for(const num of array) {
        const potsum = tar - num;
        if(potsum in nums) {
            return [potsum, num];
        }
        else {
            nums[num] = true;
        }
    }
    return [];
}
// O(nlogn) | O(1)
function twonumbersum1(array, tar) {
    array.sort((a,b) => a - b);
    let left = 0;
    let right = array.length - 1;
    while (left < right) {
        const curr = array[left] + array[right];
        if (curr === tar) {
            return [array[left], array[right]];
        }
        else if (curr < tar) {
            left++;
        }
        else if (curr > tar) {
            right--;
        }
    }
    return [];
}

console.log(twonumbersum1([2,4,6,7,8,11,42,52,13,32,21,9,1,34], 55))
