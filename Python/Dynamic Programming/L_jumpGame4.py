def minJumps(arr) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Create a dictionary to store the indices of each value in the array
        indices = defaultdict(list)
        for i, num in enumerate(arr):
            indices[num].append(i)
        
        # Initialize variables for the BFS algorithm
        visited = set()
        q = deque([(0, 0)]) # (index, steps)
        
        while q:
            index, steps = q.popleft()
            
            # Check if we have reached the end of the array
            if index == n - 1:
                return steps
            
            # Add neighbors to the queue
            for neighbor in indices[arr[index]]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, steps + 1))
            
            # Clear the list of indices for this value, since we have already visited them
            indices[arr[index]] = []
            
            # Add adjacent indices to the queue
            if index - 1 not in visited and index - 1 >= 0:
                visited.add(index - 1)
                q.append((index - 1, steps + 1))
            if index + 1 not in visited and index + 1 < n:
                visited.add(index + 1)
                q.append((index + 1, steps + 1))