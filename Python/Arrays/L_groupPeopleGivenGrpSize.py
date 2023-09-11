from typing import List


def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)
            
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []
                
        return result