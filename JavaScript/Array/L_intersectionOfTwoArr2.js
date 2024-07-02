var intersect = function (nums1, nums2) {
    const result = [];
    const track = new Map();

    // Count the elements in nums1
    for (let x of nums1) {
        track.set(x, (track.get(x) || 0) + 1);
    }

    // Find intersections with nums2
    for (let x of nums2) {
        if (track.get(x)) {
            result.push(x);
            track.set(x, track.get(x) - 1);
        }
    }

    return result;
};
