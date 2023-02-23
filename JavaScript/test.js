var data = [
    { id: "gid://shopify/Product/8139688706356" },
    {
        value: "red",
        namespace: "custom1",
        key: "color",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "2",
        namespace: "custom2",
        key: "weight",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "3",
        namespace: "custom3",
        key: "length",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "western",
        namespace: "custom4",
        key: "type",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "200",
        namespace: "custom5",
        key: "cost",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "image1",
        namespace: "custom6",
        key: "image",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "offer1",
        namespace: "custom7",
        key: "offer",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "fabric1",
        namespace: "custom8",
        key: "fabric",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "pattern1",
        namespace: "custom9",
        key: "pattern",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    {
        value: "XL",
        namespace: "custom10",
        key: "size",
        __parentId: "gid://shopify/Product/8139688706356",
    },
    { id: "gid://shopify/Product/8140158402868" },
    {
        value: "red",
        namespace: "custom1",
        key: "color",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "2",
        namespace: "custom2",
        key: "weight",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "3",
        namespace: "custom3",
        key: "length",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "western",
        namespace: "custom4",
        key: "type",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "300",
        namespace: "custom5",
        key: "cost",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "image1",
        namespace: "custom6",
        key: "image",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "offer1",
        namespace: "custom7",
        key: "offer",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "fabric1",
        namespace: "custom8",
        key: "fabric",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "pattern1",
        namespace: "custom9",
        key: "pattern",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    {
        value: "XL",
        namespace: "custom10",
        key: "size",
        __parentId: "gid://shopify/Product/8140158402868",
    },
    { id: "gid://shopify/Product/8140804391220" },
    {
        value: "red",
        namespace: "custom1",
        key: "color",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "2",
        namespace: "custom2",
        key: "weight",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "3",
        namespace: "custom3",
        key: "length",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "western",
        namespace: "custom4",
        key: "type",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "400",
        namespace: "custom5",
        key: "cost",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "image13",
        namespace: "custom6",
        key: "image",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "offer13",
        namespace: "custom7",
        key: "offer",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "fabric13",
        namespace: "custom8",
        key: "fabric",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "pattern13",
        namespace: "custom9",
        key: "pattern",
        __parentId: "gid://shopify/Product/8140804391220",
    },
    {
        value: "XLL",
        namespace: "custom10",
        key: "size",
        __parentId: "gid://shopify/Product/8140804391220",
    },
];

const Excel = require("exceljs");
const workbook = new Excel.Workbook();
const worksheet = workbook.addWorksheet("My Sheet");
var obj = {};
var arr = [];
var currid;
for (const d of data) {
    if ("id" in data) {
        // worksheet.addRow(obj);
        worksheet.addRow(obj);
        arr.push(obj);
        obj = {};
        currid = data["id"];
        obj["id"] = currid;
        continue;
    }
    obj[d.key] = d.value;
}
worksheet.addRow(obj);
console.log(arr);
console.log(worksheet);
