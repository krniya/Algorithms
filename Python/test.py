
data = open("C:\\Users\\NiYa\\Documents\\Algorithms\\Python\\data.txt", 'w+')
file = open("C:\\Users\\NiYa\\Documents\\Algorithms\\Python\\test.txt", 'r')
for each in file:
    if each[0].isalpha():
        data.write(each)


