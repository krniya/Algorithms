function findNthFib(n) {
    let fib = [0,1];
    count = 3;
    while (count <= n) {
        let newfib = fib[0] + fib[1];
        fib[0] = fib[1];
        fib[1] = newfib;
        count++;
    }
    return n > 1 ? fib[1] : fib[2];
}