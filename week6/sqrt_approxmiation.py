from secret_data import  secret_number
epsilon = 0.01
increment = 0.001
guess = 0.0
num_guesses = 0
while abs(guess**2 - secret_number) >= epsilon and guess <= secret_number:
    guess += increment
    num_guesses += 1
    if abs(guess**2 - secret_number) >= epsilon:
        print(f"Failed to find square root of {secret_number}")
    else:
        print(f"Square root of {secret_number} is about {guess:.0f} ({num_guesses} guesses)")