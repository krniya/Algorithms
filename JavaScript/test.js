let a = {
    name: { n: "Nitish" },
};

for (let i = 0; i < 5; i++) {
    a["name" + i] = i;
}
console.log(a);
