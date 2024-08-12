class KthLargest {
    constructor(k, nums) {
        this.k = k;
        this.minHeap = new MinPriorityQueue();
        for (let num of nums) {
            this.add(num);
        }
    }

    add(val) {
        if (this.minHeap.size() < this.k) {
            this.minHeap.enqueue(val);
        } else if (val > this.minHeap.front().element) {
            this.minHeap.dequeue();
            this.minHeap.enqueue(val);
        }
        return this.minHeap.front().element;
    }
}
