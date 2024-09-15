var findTheLongestSubstring = function (s) {
    let n = s.length;
    let mask = 0;
    let maxLength = 0;
    let m = new Map();
    m.set(0, -1);

    for (let i = 0; i < n; i++) {
        if (s[i] === "a") mask ^= 1 << 0;
        else if (s[i] === "e") mask ^= 1 << 1;
        else if (s[i] === "i") mask ^= 1 << 2;
        else if (s[i] === "o") mask ^= 1 << 3;
        else if (s[i] === "u") mask ^= 1 << 4;

        if (m.has(mask)) {
            maxLength = Math.max(maxLength, i - m.get(mask));
        } else {
            m.set(mask, i);
        }
    }

    return maxLength;
};
