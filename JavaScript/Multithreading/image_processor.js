const { parentPort } = require("worker_threads");

function simulateBlur(imageData) {
    // This is a simplified blur simulation
    // In a real application, you'd implement a proper blur algorithm
    return imageData.map((pixel, index, array) => {
        if (index === 0 || index === array.length - 1) return pixel;
        return Math.floor((array[index - 1] + pixel + array[index + 1]) / 3);
    });
}

parentPort.on("message", (images) => {
    const processedImages = images.map((image) => ({
        id: image.id,
        data: simulateBlur(image.data),
    }));

    parentPort.postMessage(processedImages);
});
