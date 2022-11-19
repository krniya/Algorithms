def outerTrees(trees):
        trees = sorted(trees)                                    # [1] make an x-ordered list of points
        #trees = [np.array(t) for t in sorted(trees)]            #     (for a numpy solution, use this)
        U, L = [], []
        
        def cross(B, A, T):                                      # [2] this function computes cross product
            Bx, By, Ax, Ay, Tx, Ty = chain(B, A, T)              #     between vectors BT=T-B and AB=B-A
            return (Ty-By)*(Bx-Ax) - (By-Ay)*(Tx-Bx)
            #return np.cross(T-B,B-A)                            #     (for a numpy solution, use this)
                
        for T in trees:                                          # [3] according to Andrew's algorithm,
            while len(U) >= 2 and cross(U[-1],U[-2],T) < 0:      #     we add points to upper (lower)
                U.pop()                                          #     convex hulls if they make a
            U.append(T)                                          #     clockwise (counterclockwise) turn
                                                                 #     with respect to the last two trees
            while len(L) >= 2 and cross(L[-1],L[-2],T) > 0:      #     in the convex hull; if that's not
                L.pop()                                          #     possible, we first remove all previous
            L.append(T)                                          #     trees that break the convexity

        return set(tuple(T) for T in (U+L))