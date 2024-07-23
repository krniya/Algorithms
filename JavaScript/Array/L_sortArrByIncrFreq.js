function frequencySort(nums) {
    let count = Array(201).fill(0);
    nums.forEach((num) => {
        count[num + 100]++;
    });
    return nums.sort((a, b) => {
        if (count[a + 100] === count[b + 100]) {
            return b - a;
        }
        return count[a + 100] - count[b + 100];
    });
}
