def minJumps(arr, n):
	count = i = 0
	while i < n - 1:
	    if arr[i] == 0:
	        return -1
	    i += arr[i]
	    count += 1
	return count

print(minJumps([2, 3, 1, 1, 2, 4, 2, 0, 1, 1], 10))