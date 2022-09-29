def findClosestElements(arr , k: int, x: int):
        if len(arr) == k:
            return arr
        l, r = 0, len(arr) - k
        mid = 0
        while l < r:
            
            mid = (l + r) // 2
            print(l, mid, r)
			#we want to line up mid with the ideal left for our window
			
            if (x - arr[mid]) > (arr[mid + k] - x):
                l = mid + 1
            
            else:
                r = mid
            
		#return the window we have been working with
        return arr[l: l + k]