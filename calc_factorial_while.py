# Kullanıcıdan bir sayı alıyoruz
sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))

# İşlemde sayının orijinal değerini kaybetmemek için kopya oluşturuyoruz
gecici_sayi = sayi
faktoriyel = 1

# Sayı 0'dan büyük olduğu sürece döngü devam edecek
while gecici_sayi > 0:
    faktoriyel *= gecici_sayi
    gecici_sayi -= 1  # Sayıyı her adımda 1 azaltıyoruz

# Sonucu ekrana yazdırıyoruz
print(f"{sayi}! = {faktoriyel}")