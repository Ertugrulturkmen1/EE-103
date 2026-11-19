import secret_number
guess = int(input("Enter your guess: "))
while guess != secret_number.secretNum:
    
    if guess < secret_number.secretNumr:
        print("Too low!")
    elif guess > secret_number.secretNum:
        print("Too high!")
    else:
        print("Congratulations! You guessed the secret number.")    
    