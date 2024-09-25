var procreate = require("procreate-swatch-generator");

procreate(
    [
        "#114678",

        "#256a9c",

        "#4fa5b5",

        "#f7f7da",

        "#85bbbb",

        "#fdfbbd",

        "#67a19a",

        "#3c7b95",

        "#47865b",

        "#a99a8e",

        "#234f5d",

        "#3d754a",

        "#cacd56",

        "#143a3f",

        "#697570",

        "#33617f",

        "#426e89",

        "#4b6579",

        "#e4b876",

        "#ffef8f",

        "#0e3634",

        "#1d493e",

        "#356435",

        "#a7a838",

        "#e4ec52",

        "#0b2743",

        "#0b2e40",

        "#1a3c37",

        "#c7873e",

        "#eb9b81",
    ],
    "Tree Land"
).pipe(require("fs").createWriteStream("./Tree Land.swatches"));
