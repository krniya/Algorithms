from collections import defaultdict, deque


def amountOfTime(root, start: int) -> int:
    def dfs(node):
        if node is None:
            return
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
        dfs(node.left)
        dfs(node.right)

    graph = defaultdict(list)
    dfs(root)
    visited = set()
    queue = deque([start])
    time = -1
    while queue:
        time += 1
        for _ in range(len(queue)):
            current_node = queue.popleft()
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return time