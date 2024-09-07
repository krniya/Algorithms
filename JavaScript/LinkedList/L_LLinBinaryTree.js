var isSubPath = function (head, root) {
    return dfs(head, head, root);
};

var dfs = function (head, cur, root) {
    if (cur === null) return true; // Successfully matched the list
    if (root === null) return false; // Reached the end of the tree without matching

    if (cur.val === root.val) {
        cur = cur.next; // Move to the next list node if value matches
    } else if (head.val === root.val) {
        head = head.next; // Start new matching attempt if the value matches head of list
    } else {
        cur = head; // Reset the matching pointer
    }

    // Recursively check left and right subtrees
    return dfs(head, cur, root.left) || dfs(head, cur, root.right);
};
