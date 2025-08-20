secret = 7

while true:
    guess = int(("secret number: "))
    
    if guess < secret:
        print("low")
    elif guess > secret:
        print("high")
    else:
        print("congratulations, you guessed correctly")