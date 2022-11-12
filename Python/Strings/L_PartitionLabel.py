def partitionLabels(s):
    rightmost = {c:i for i, c in enumerate(s)}
    left, right = 0, 0
    result = []
    for i, letter in enumerate(s):
        right = max(right,rightmost[letter])
        if i == right:
            result += [right-left + 1]
            left = i+1
    return result



def partitionLabels(s):
        lastIndex = {}
        for idx, ch in enumerate(s):
            lastIndex[ch] = idx
        res = []
        size = end = 0
        for idx, ch in enumerate(s):
            size += 1
            end = max(end, lastIndex[ch])
            if idx == end:
                res.append(size)
                size = 0
        return res

print(partitionLabels("ababcbacadefegdehijhklij"))