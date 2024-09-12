var countConsistentStrings = function (allowed, words) {
    const arr = Array(26).fill(false);
    for (let w of allowed) {
        let idx = w.charCodeAt(0) - "97";
        //console.log(idx)
        arr[idx] = true;
    }
    let cnt = 0;
    for (let word of words) {
        for (let ch of word) {
            let idx = ch.charCodeAt(0) - "97";
            if (arr[idx] === false) {
                cnt++;
                break;
            }
        }
    }
    return words.length - cnt;
};
