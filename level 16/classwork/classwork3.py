number1 = int(input("enter first number"))
number2 = int(input("enter second number"))

if number1 > number2:
    print("first number is more")
else:
    if number1 < number2:
        print("second number is more")
    else:
        print("both numbers are equal")