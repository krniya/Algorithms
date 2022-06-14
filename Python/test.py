# def secLarDiff(arr):
#     arr.sort()
#     return max(arr[-1]-arr[1],arr[-2]-arr[0])

# print(secLarSum([14,12,70,15,95,65,22,30]))

# def replacer(str):
#     li= str.split(".")
#     rep = "xyz"
#     for i in range(1,len(li),2):
#         li[i] = rep
#     return ".".join(li)

# print(replacer("i.love.this.progam.very.much"))

# def counter(s):
#     s = s.lower()
#     hm = {}
#     for ch in s:
#         if ch not in hm:
#             hm[ch] = 1
#         else:
#             hm[ch] += 1
#     chk = "bfjpv"
#     res = []
#     tot = 0
#     for ch in chk:
#         if ch in hm:
#             a = hm[ch]
#             res.append(ch + "=" + str(a))
#             tot += hm[ch]
#     res.append("Total="+str(tot))
#     return " ".join(res)

# print(counter("raJasoftwarelaBs"))

def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def primeSum(arr):
    sum = 0
    for n in arr:
        if not isPrime(n):
            sum+=n
    return sum

print(primeSum([2,10,13,9]))
        