from collections import defaultdict


def findDuplicate(paths):
        pMap = defaultdict(list)
        res = []
        for path in paths:
            curr = path.split(" ")
            dir = curr.pop(0)
            dir += "/"
            for files in curr:
                file = files.split("(")
                file[1] = file[1][:-1]
                pMap[file[1]].append((dir + file[0]))
        for key, val in pMap.items():
            if len(val) > 1:
                res.append(val)
        return res

print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))