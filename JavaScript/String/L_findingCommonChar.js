var count = function (word) {
    const frequency = Array(26).fill(0);
    for (let char of word) {
        frequency[char.charCodeAt(0) - "a".charCodeAt(0)]++;
    }
    return frequency;
};

var intersection = function (freq1, freq2) {
    return freq1.map((f1, idx) => Math.min(f1, freq2[idx]));
};

var commonChars = function (words) {
    let last = count(words[0]);
    for (let i = 1; i < words.length; i++) {
        last = intersection(last, count(words[i]));
    }

    const result = [];
    for (let i = 0; i < 26; i++) {
        while (last[i] > 0) {
            result.push(String.fromCharCode(i + "a".charCodeAt(0)));
            last[i]--;
        }
    }

    return result;
};
