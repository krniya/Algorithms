var uncommonFromSentences = function (s1, s2) {
    let set = new Set();
    let dupset = new Set();
    s1 = s1.split(" ");
    s2 = s2.split(" ");
    for (let x of s1) {
        if (!dupset.has(x)) {
            if (set.has(x)) {
                set.delete(x);
                dupset.add(x);
            } else set.add(x);
        }
    }
    for (let x of s2) {
        if (!dupset.has(x)) {
            if (set.has(x)) {
                set.delete(x);
                dupset.add(x);
            } else set.add(x);
        }
    }
    return Array.from(set);
};
