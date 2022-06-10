def isMatch(self, s, t):
    if not(s and t):
        return s is t
    return (s.val == t.val and 
            self.isMatch(s.left, t.left) and 
            self.isMatch(s.right, t.right))

def isSubtree(self, s, t):
    if self.isMatch(s, t): return True
    if not s: return False
    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


def isSubtree(t, s) -> bool:
        if not t: return True
        if not s: return False
        if sameTree(s,t):
            return True
        return (isSubtree(s.left, t) or isSubtree(s.right, t))
        
def sameTree( s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (sameTree(s.left, t.left) and sameTree(s.right, t.right))
        return False

