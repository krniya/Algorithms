import re
s = "A man, a plan, a canal: Panama"
str = re.findall("[A-Za-z]", s.lower())
print(str)