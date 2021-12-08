import sys
def findCommon(ar1, ar2, ar3, n1,n2, n3) :
    i =j=k= 0
    prev1 = prev2 = prev3 = -sys.maxsize - 1
    while (i < n1 and j < n2 and k < n3) :
        while (ar1[i] == prev1 and i < n1-1) :
            i += 1
        while (ar2[j] == prev2 and j < n2) :
            j += 1
        while (ar3[k] == prev3 and k < n3) :
            k += 1
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]) :
            print(ar1[i],end=" ")
            prev1 = ar1[i]
            prev2 = ar2[j]
            prev3 = ar3[k]
            i += 1
            j += 1
            k += 1
        elif (ar1[i] < ar2[j]) :
            prev1 = ar1[i]
            i += 1
        elif (ar2[j] < ar3[k]) :
            prev2 = ar2[j]
            j += 1
        else :
            prev3 = ar3[k]
            k += 1
 