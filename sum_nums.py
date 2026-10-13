# Kullanıcıdan bir sayı alıyoruz
num = int(input("Bir sayı girin: "))

# Döngü ile toplamı hesaplama
toplam = 0
for i in range(1, num + 1):
    toplam += i

# Gauss toplama kuralı ile hesaplama (n * (n + 1) / 2)
sum_gauss = num * (num + 1) / 2

# İki sonucun eşit olup olmadığını kontrol etme
if toplam == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")