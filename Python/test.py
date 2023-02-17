number = int(input("Enter a number: "))
if number % 11 == 0:
    print("Foo")
elif number % 17 == 0:
    print("Bar")
elif number % 11 == 0 and number % 17 == 0:
    print("Foo Bar")