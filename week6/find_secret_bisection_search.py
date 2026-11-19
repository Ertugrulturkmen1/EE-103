from secret_data import secret_year
guesses = 0
low_bound = 0
high_bound = 2026
guess = (low_bound + high_bound) // 2
while guess != secret_year:
    if guess < secret_year:
        low_bound = guess + 1
    elif guess > secret_year:
        high_bound = guess - 1
    guess = (low_bound + high_bound) // 2
    guesses += 1
print(f"You found the secret year: {guess}")
print(f"Number of guesses using bisection search: {guesses}")