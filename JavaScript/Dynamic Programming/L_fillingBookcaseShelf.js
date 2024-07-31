/**
 * @param {number[][]} books
 * @param {number} shelfWidth
 * @return {number}
 */
var minHeightShelves = function (books, shelfWidth) {
    return arrangeBooks(books, shelfWidth);
};

/**
 * @param {number[][]} books
 * @param {number} maxShelfWidth
 * @return {number}
 */
function arrangeBooks(books, maxShelfWidth) {
    const minHeights = new Array(books.length + 1).fill(Infinity);
    minHeights[0] = 0;

    for (let bookIndex = 1; bookIndex <= books.length; bookIndex++) {
        let currentShelfHeight = 0;
        let currentShelfWidth = 0;

        for (let lastBook = bookIndex - 1; lastBook >= 0; lastBook--) {
            const [currentBookThickness, currentBookHeight] = books[lastBook];

            if (currentShelfWidth + currentBookThickness > maxShelfWidth) {
                break;
            }

            currentShelfWidth += currentBookThickness;
            currentShelfHeight = Math.max(currentShelfHeight, currentBookHeight);

            const currentArrangementHeight = minHeights[lastBook] + currentShelfHeight;
            minHeights[bookIndex] = Math.min(minHeights[bookIndex], currentArrangementHeight);
        }
    }

    return minHeights[books.length];
}
