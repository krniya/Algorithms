const { Worker } = require("worker_threads");

const jobs = new Array(100).fill(1e9);

const chunkify = (jobs, threads) => {
    const chunks = [];
    for (let i = threads; i > 0; i--) {
        chunks.push(jobs.splice(0, Math.ceil(jobs.length / i)));
    }
    return chunks;
};

const run_job = (jobs, threads) => {
    const chunks = chunkify(jobs, threads);
    let currentJob = 0;
    const start = performance.now();
    chunks.forEach((job, i) => {
        const worker = new Worker("./JavaScript/Multithreading/worker.js");
        worker.postMessage(job);

        worker.on("message", () => {
            console.log(`Task ${i} completed`);
            currentJob++;
            if (currentJob == threads) {
                console.log(
                    `Above task took ${performance.now() - start}ms using ${threads} threads`
                );
                process.exit();
            }
        });
    });
};

run_job(jobs, 16);

// const start = performance.now();

// for (let job of jobs) {
//     let count = 0;
//     for (let i = 0; i < job; i++) count++;
// }

// const end = performance.now();

// console.log(`Time taken by above task ${end - start} ms`);
