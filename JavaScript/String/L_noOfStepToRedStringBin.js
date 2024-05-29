var numSteps = function (s) {
    let steps = 0,
        carry = 0;
    for (let i = s.length - 1; i > 0; i--) {
        if (s.charAt(i) - "0" + carry == 1) {
            carry = 1;
            steps += 2;
        } else {
            steps++;
        }
    }
    return carry + steps;
};
