var createHelloWorld = function () {
    return function (...args) {
        return "Hello World";
    };
};

const f = createHelloWorld();
console.log(f()); // "Hello World"
