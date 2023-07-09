def largestVariance(s: str) -> int:
        res = 0
        chars = list(set(s))
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                c1, c2 = chars[i], chars[j]
				
				# keep track of count(c1) - count(c2) 
                diff = 0 
				
				# max and min of diff
				# result should be maximum of (diff - min_diff, max_diff - diff)
				# e.g. "baabaa", at index = 0, min_diff = -1. when index = 5, diff = 4 - 2 = 2, result = diff - min_diff = 2 - (-1) = 3
                max_diff = min_diff = 0
				
				# diff at the previous occurance of c1/c2
                last_c1_diff = last_c2_diff = 0 
				
				# check wether we have met c1/c2 during the loop
                meet_c1 = meet_c2 = False
				
                for c in s:
                    if c == c1:
                        meet_c1 = True
                        diff += 1
						
						#  use last_c1_diff instead of diff because we have to make sure that c1 is in the rest part of the substring. 
						# e.g. [c1, c1, c2, c2, c2]
						# At index = 1, if we use diff = 2 -> max_diff = 2
						# At index = 4, diff = 2 - 3 = -1, result = max_diff - diff = 3. 
						# Though we have [c2, c2, c2] as a substring, c1 is not in this string and the result is invalid
                        max_diff = max(last_c1_diff, max_diff)
						
                        last_c1_diff = diff
                    elif c == c2:
                        meet_c2 = True
                        diff -= 1
                        min_diff = min(last_c2_diff, min_diff)
                        last_c2_diff = diff
                    else:
                        continue
					
					# update the result only when we have met both c1 and c2 
                    if meet_c1 and meet_c2:
                        res = max(diff - min_diff, max_diff - diff, res)
        return res

def largestVariance1(s: str) -> int:
        res = 0
        unique = set(sorted(s))
        for a in unique:
            for b in unique:
                var = has_b = first_b = 0
                for ch in s:
                    var+= ch == a
                    if ch == b:
                        has_b = True
                        if first_b and var >= 0:
                            first_b = False
                        elif var - 1 < 0:
                            first_b = True
                            var = -1
                if has_b:
                    res = max(res, var)
                else:
                    res = max(res, 0)
        return res
                        

print(largestVariance1("aabbbbaabbbaaaaba"))

def largestVariance(self, s: str) -> int:
        count1 = 0
        count2 = 0
        max_variance = 0
        
        # create distinct list of character pairs
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]

        # run once for original string order, then again for reverse string order
        for runs in range(2):
            for pair in pairs:
                count1 = count2 = 0
                for letter in s:
                    # no reason to process letters that aren't part of the current pair
                    if letter not in pair:
                        continue
                    if letter == pair[0]:
                        count1 += 1
                    elif letter == pair[1]:
                        count2 += 1
                    if count1 < count2:
                        count1 = count2 = 0
                    elif count1 > 0 and count2 > 0:
                        max_variance = max(max_variance, count1 - count2)
                
            
            # reverse the string for the second time around
            s = s[::-1]
                
        return max_variance