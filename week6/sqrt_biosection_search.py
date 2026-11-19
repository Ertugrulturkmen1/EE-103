from secret_data import secret_number
epsilon = 0.01
low_bound = 0.0
high_bound = secret_number
num_guesses = 0
guess = (low_bound + high_bound) / 2
while abs(guess**2 - secret_number) >= epsilon:
    if guess**2 < secret_number:
        low_bound = guess
    else:
        high_bound = guess
    guess = (low_bound + high_bound) / 2
    num_guesses += 1
    print(f"result of bisection search: {guess:.3f}")
    print(f"number of guesses using bisection search: {num_guesses}")