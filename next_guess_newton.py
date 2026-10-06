x = float(input("What x to find the square root of? "))
guess = float(input("What guess to start with? "))

print(guess**2)

next_guess = guess - (guess**2 - x) / (2 * guess)
print(next_guess)