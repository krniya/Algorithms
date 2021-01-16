function threeLargestNo(array) {
    let threeLarNum = [null, null, null];
    for (const ele in array) {
        threeLarHelper(threeLarNum, ele);
    }
    return threeLarNum;
}

function threeLarHelper(array, ele) {
    if (threeLargest[2] === null || num > threeLargest[2]) {
        shiftAndUpdate(threeLargest, num, 2);
    } else if (threeLargest[1] === null || num > threeLargest[1]) {
        shiftAndUpdate(threeLargest, num, 1);
    } else if (threeLargest[0] === null || num > threeLargest[0]) {
        shiftAndUpdate(threeLargest, num, 0);
    }
}

function shiftAndUpdate(array, num, idx) {
    for (let i = 0; i <= idx; i++) {
        if (i === idx) {
            array[i] = num;
        } else {
            array[i] = array[i + 1];
        }
    }
}