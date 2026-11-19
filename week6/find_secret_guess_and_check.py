
from secret_data import secret_year

guesses = 0
guess = 0

while guess != secret_year:
    guess += 1
    guesses += 1

print(f"Bulunan gizli yıl: {guess}")
print(f"Guess-and-check algoritması tahmin sayısı: {guesses}")

