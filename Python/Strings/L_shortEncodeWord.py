def minimumLengthEncoding(words) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)


def minimumLengthEncoding1(words) -> int:
        trie, ans = {}, 0
        for word in words:
            node = trie
            for c in reversed(word):
                if '$' in node: ans -= node.pop('$')
                node = node.setdefault(c, {})
            if not node:
                node['$'] = len(word) + 1
                ans += node['$']
        return ans

print(minimumLengthEncoding1(["time", "me", "bell"]))