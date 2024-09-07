/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function (nums, head) {
    let max = -1;
    for (let num of nums) {
        max = num > max ? num : max;
    }

    let freq = new Array(max + 1).fill(false);

    for (let num of nums) freq[num] = true;

    let temp = new ListNode();
    let current = temp;

    while (head != null) {
        if (head.val >= freq.length || freq[head.val] == false) {
            current.next = head;
            current = current.next;
        }
        head = head.next;
    }

    current.next = null;
    return temp.next;
};
