# O(min(m,n)) |
def isIsomorphic(n1, n2):
    if n2 is None and n2 is None:
        return True

    if n1 is None or n2 is None:
        return False

    if n1.data != n2.data:
        return False

    return ((isIsomorphic(n1.left, n2.left) and
             isIsomorphic(n1.right, n2.right)) or
            (isIsomorphic(n1.left, n2.right) and
             isIsomorphic(n1.right, n2.left)))
