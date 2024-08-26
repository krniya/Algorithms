var postorder = function (root) {
    let post_res = [];
    var post = function (node) {
        if (!node) return null;
        for (let child of node.children) {
            post(child);
        }
        post_res.push(node.val);
    };
    post(root);
    return post_res;
};
