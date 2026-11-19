import secret_number
trails = 0
guess = 0
while guess != secret_number.secretNum:
    guess = int(input("Enter your guess: "))
    trails += 1
    if guess < secret_number.secretNum:
        print(guess)
    elif guess > secret_number.secretNum:
        print(guess)
    else:
     print("Congratulations! You guessed the secret number.")    
     break
    while trails == 5:
        print("oh noooo...")

