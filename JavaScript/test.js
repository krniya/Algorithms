var time = 1000;
var count = 1;

while (count < 15) {
    setTimeout(function () {
        console.log(count);
    }, time * count);
    count++;
}
