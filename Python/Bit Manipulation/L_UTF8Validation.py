def validUtf8(data) -> bool:
        k = 0
        while k < len(data):
		# we are doing right shift like n>>5(n=1000 0000) and we will get 100 i.e 3 digit from the start.
			
            if data[k] >> 7 == 0:
                k += 1
            elif data[k] >> 5 == 0b110:
		# if the 8-5=3 digit is 110(from the start) it means it is 2 bytes so we need n-1 i.e 1 10xx sequence so k+=2
                if k+1 == len(data) or data[k+1] >> 6 != 0b10:
                    return False
                k += 2
            elif data[k] >> 4 == 0b1110:
                if k+2 >= len(data) or data[k+1] >> 6 != 0b10 or data[k+2] >> 6 != 0b10:
                    return False
                k += 3
            elif data[k] >> 3 == 0b11110:
                if k+3 >= len(data) or data[k+1] >> 6 != 0b10 or data[k+2] >> 6 != 0b10 or data[k+3] >> 6 != 0b10:
                    return False
                k += 4
            else:
                return False
        return True