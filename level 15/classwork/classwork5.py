secret = 7
guess = int(input("guess the number: "))

while guess != secret:
    if guess < secret:
        print("low. try more high number. ")
    elif guess > secret:
        print("high. try more low number. ")
    else:
        print("guess. ")
