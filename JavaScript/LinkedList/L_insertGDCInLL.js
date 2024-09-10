var insertGreatestCommonDivisors = function (head) {
    if (!head || !head.next) return head;

    const gcd = (a, b) => {
        while (b !== 0) {
            [a, b] = [b, a % b];
        }
        return a;
    };

    let node1 = head;
    while (node1.next) {
        let node2 = node1.next;
        let gcdValue = gcd(node1.val, node2.val);
        let gcdNode = new ListNode(gcdValue);
        node1.next = gcdNode;
        gcdNode.next = node2;
        node1 = node2;
    }

    return head;
};
