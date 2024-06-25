var bstToGst = function (root) {
    let sum = 0;

    const traverse = (node) => {
        if (node) {
            traverse(node.right); // Traverse the right subtree
            sum += node.val; // Update the sum
            node.val = sum; // Update the current node's value
            traverse(node.left); // Traverse the left subtree
        }
    };

    traverse(root);
    return root;
};
