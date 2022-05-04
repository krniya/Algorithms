def letterCombinations(digits: str):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}    
        result = []
        
        def helpCombine(current, leftoverDigits):
            if not leftoverDigits:
                result.append(current)
                return 
            else:
                for char in phone[leftoverDigits[0]]:
                    helpCombine(current + char, leftoverDigits[1:])
        
        if not digits:
            return []
        else: 
            helpCombine("", digits)
            return result