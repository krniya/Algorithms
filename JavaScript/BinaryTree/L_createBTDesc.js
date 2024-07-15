var createBinaryTree = function (descriptions) {
    let childrenSet = new Set();
    let childrenHashmap = new Map();

    for (let [parent, child, isLeft] of descriptions) {
        if (!childrenHashmap.has(parent)) {
            childrenHashmap.set(parent, [-1, -1]);
        }

        childrenSet.add(child);

        if (isLeft === 1) {
            childrenHashmap.get(parent)[0] = child;
        } else {
            childrenHashmap.get(parent)[1] = child;
        }
    }

    let headNodeVal;
    for (let parent of childrenHashmap.keys()) {
        if (!childrenSet.has(parent)) {
            headNodeVal = parent;
            break;
        }
    }

    return constructTree(headNodeVal, childrenHashmap);
};

function constructTree(curNodeVal, childrenHashmap) {
    let newNode = new TreeNode(curNodeVal);
    if (childrenHashmap.has(curNodeVal)) {
        let [left, right] = childrenHashmap.get(curNodeVal);
        if (left !== -1) {
            newNode.left = constructTree(left, childrenHashmap);
        }
        if (right !== -1) {
            newNode.right = constructTree(right, childrenHashmap);
        }
    }
    return newNode;
}
