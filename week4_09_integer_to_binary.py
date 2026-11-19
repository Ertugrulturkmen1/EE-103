# Tam sayıyı ikili (binary) sisteme çevirme
sayi = 13
ikili_sonuc = ""

while sayi > 0:
    kalan = sayi % 2
    ikili_sonuc = str(kalan) + ikili_sonuc
    sayi = sayi // 2

print(f'"13" converted to binary is "{ikili_sonuc}"')
