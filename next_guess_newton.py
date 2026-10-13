# 1. Kullanıcıdan x değerini al
x = float(input("What x to find the cube root of? "))

# 2. Kullanıcıdan başlangıç tahminini (guess) al
guess = float(input("What guess to start with? "))

# 3. Mevcut tahminin küpünü yazdır
print("Current estimate cube:", guess ** 3)

# 4. Yeni tahmini Newton yöntemiyle hesapla
next_guess = guess - (guess ** 3 - x) / (3 * guess ** 2)

# 5. Yeni tahmini ekrana yazdır
print("Next guess:", next_guess)
