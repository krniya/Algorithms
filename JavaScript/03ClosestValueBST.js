function closestValueBst(tree, target) {
    return closestHelper(tree, target, Infinity);
}

function closestHelper(tree, target, closest) {
    let current = tree;
    while (current != null) {
        if(Math.abs(target - closest) > Math.abs(target - current.value)) {
            closest = current.value;
        }
        if(target < current.value) {
            current = current.left;
        }
        else if (target > current.value) {
            current = current.right;
        }
        else {
            break;
        }
    }
    return closest;
}