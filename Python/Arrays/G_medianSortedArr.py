def medianSortedArr(ar1, ar2):
    n = len(ar1)
    m = len(ar2)
    i = 0
    j = 0 
    m1, m2 = -1, -1
    if((m + n) % 2 == 1) :   
        for count in range(((n + m) // 2) + 1) :       
            if(i != n and j != m) :           
                if ar1[i] > ar2[j] :
                    m1 = ar2[j]
                    j += 1
                else :
                    m1 = ar1[i]
                    i += 1           
            elif(i < n) :           
                m1 = ar1[i]
                i += 1
            else :           
                m1 = ar2[j]
                j += 1       
        return m1
    else :
        for count in range(((n + m) // 2) + 1) :        
            m2 = m1
            if(i != n and j != m) :       
                if ar1[i] > ar2[j] :
                    m1 = ar2[j]
                    j += 1
                else :
                    m1 = ar1[i]
                    i += 1           
            elif(i < n) :           
                m1 = ar1[i]
                i += 1
            else :           
                m1 = ar2[j]
                j += 1       
        return (m1 + m2)//2



print(medianSortedArr([-5,-2,4,7,10,14], [-9,-3,2,6,9,13]))