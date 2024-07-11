var reverseParentheses = function (s) {
    const stack = [];

    for (let i = 0; i < s.length; i++) {
        const char = s.charAt(i);

        if (char === ")") {
            let rev = "";
            while (stack.length > 0 && stack[stack.length - 1] != "(") rev += stack.pop();
            stack.pop();

            for (let i = 0; i < rev.length; i++) stack.push(rev.charAt(i));
        } else stack.push(char);
    }
    return stack.join("");
};
