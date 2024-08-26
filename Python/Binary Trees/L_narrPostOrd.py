def postorder(root) :
    post_res = []
    def post(node):
        if not node:
            return
        for child in node.children:
            post(child)
        post_res.append(node.val)
    post(root)
    return post_res