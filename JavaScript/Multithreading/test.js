const jobs = new Array(100).fill(1e9);

const { Worker } = require("worker_threads");

const chunkify = (jobs, partiton) => {
    let chunks = [];
    for (let i = partiton; i > 0; i--) {
        chunks.push(jobs.splice(0, Math.ceil(jobs.length / i)));
    }
    return chunks;
};

const job_runner = (jobs, threads) => {
    const chunks = chunkify(jobs, threads);
    const start = performance.now();
    let currentJob = 0;
    chunks.forEach((job, i) => {
        const worker = new Worker("./work.js");
        worker.postMessage(job);
        worker.on("message", () => {
            console.log(`Task ${i} completed`);
            currentJob++;
            if (currentJob == threads) {
                console.log(`${threads} Threads took ${performance.now() - start} ms`);
                process.exit();
            }
        });
    });

    // const end = performance.now();
    // console.log(`Above task took ${end - start}ms`);
};

job_runner(jobs, 10);

// const start = performance.now();

// for (let job of jobs) {
//     let count = 0;
//     for (let i = 0; i < job; i++) count++;
// }

// const end = performance.now();

// console.log(`Above task took ${end - start}ms`);
