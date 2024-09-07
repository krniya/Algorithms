const { parentPort } = require("worker_threads");

parentPort.on("message", (jobs) => {
    let count = 0;
    for (let job of jobs) {
        for (let i = 0; i < job; i++) count++;
    }

    parentPort.postMessage("Done");
});
