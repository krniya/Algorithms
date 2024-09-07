const { Worker } = require("worker_threads");

const jobs = Array.from({ length: 1000 }, () => 1e9);

function chunkify(array, n) {
    let chunks = [];
    for (let i = n; i > 0; i--) {
        chunks.push(array.splice(0, Math.ceil(array.length / i)));
    }
    return chunks;
}

function run(jobs, concurrentWorkers) {
    const chunks = chunkify(jobs, concurrentWorkers);
    const start = performance.now();
    let completedWorker = 0;
    chunks.forEach((data, i) => {
        const worker = new Worker("./worker.js");
        worker.postMessage(data);
        worker.on("message", () => {
            console.log(`Worker ${i} completed`);
            completedWorker++;
            if (completedWorker === concurrentWorkers) {
                console.log(`${concurrentWorkers} workers took ${performance.now() - start}ms`);
                process.exit();
            }
        });
    });
}

run(jobs, 16);
