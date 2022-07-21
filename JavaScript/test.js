const xlsx = require("xlsx");
const filepath = "./data.xlsx";

const xlsxToJson = (filePath, sheetName) => {
    const workbook = xlsx.readFile(filePath);
    const sheet = workbook.Sheets[sheetName];
    return xlsx.utils.sheet_to_json(sheet);
};

const jsonSheet = xlsxToJson("./data.xlsx", "Sheet1");
console.log(jsonSheet);

// function readFile(f) {
//     var name = f.name;
//     const reader = new FileReader();
//     reader.onload = (evt) => {
//         const bstr = evt.target.result;
//         const wb = XLSX.read(bstr, { type: "binary" });
//         const wsname = wb.SheetNames[0];
//         const ws = wb.Sheets[wsname];
//         const data = XLSX.utils.sheet_to_csv(ws, { header: 1 });
//         console.log("Data>>>" + data);
//         console.log(this.convertToJson(data));
//     };
//     reader.readAsBinaryString(f);
// }

// function convertToJson(csv) {
//     var lines = csv.split("\n");
//     var result = [];
//     var headers = lines[0].split(",");
//     for (var i = 1; i < lines.length; i++) {
//         var obj = {};
//         var currentline = lines[i].split(",");
//         for (var j = 0; j < headers.length; j++) {
//             obj[headers[j]] = currentline[j];
//         }
//         result.push(obj);
//     }
//     return JSON.stringify(result);
// }
