# Kullanıcıdan bir sayı alıyoruz
sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))

# Sonucu tutacağımız değişken
faktoriyel = 1

# 1'den girilen sayıya kadar (sayı dahil) olan sayıları çarpıyoruz
for i in range(1, sayi + 1):
    faktoriyel *= i

# Sonucu ekrana yazdırıyoruz
print(f"{sayi}! = {faktoriyel}")