const { Worker } = require("worker_threads");
const path = require("path");

// Simulated image data (arrays of numbers representing pixel values)
const images = [
    { id: 1, data: new Array(1000000).fill(0).map(() => Math.floor(Math.random() * 256)) },
    { id: 2, data: new Array(1000000).fill(0).map(() => Math.floor(Math.random() * 256)) },
    { id: 3, data: new Array(1000000).fill(0).map(() => Math.floor(Math.random() * 256)) },
    { id: 4, data: new Array(1000000).fill(0).map(() => Math.floor(Math.random() * 256)) },
];

function createWorker(imagesForThread) {
    return new Promise((resolve, reject) => {
        const worker = new Worker(path.join(__dirname, "image_processor.js"));
        worker.postMessage(imagesForThread);

        worker.on("message", (processedImages) => {
            resolve(processedImages);
        });

        worker.on("error", reject);
    });
}

async function processImagesMultithreaded(images, numThreads) {
    const start = performance.now();
    const workerPromises = [];

    for (let i = 0; i < numThreads; i++) {
        const imagesForThread = images.filter((_, index) => index % numThreads === i);
        workerPromises.push(createWorker(imagesForThread));
    }

    const results = await Promise.all(workerPromises);
    const processedImages = results.flat();

    const end = performance.now();
    console.log(`Multithreaded processing completed in ${end - start} ms`);

    return processedImages;
}

async function main() {
    console.log("Starting image processing...");
    try {
        const processedImages = await processImagesMultithreaded(images, 4);
        console.log(`Processed ${processedImages.length} images`);
        // In a real application, you might save the processed images here
    } catch (error) {
        console.error("Error processing images:", error);
    }
}

main();
