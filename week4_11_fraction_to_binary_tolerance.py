# Hata Paylı Kesir Çevrimi
hedef_kesir = 0.1
kesir = hedef_kesir
ikili_kesir = "0."
mevcut_deger = 0.0
adim = 1

while abs(mevcut_deger - hedef_kesir) >= 0.00001:
    kesir *= 2
    tam_kisim = int(kesir)
    ikili_kesir += str(tam_kisim)
    kesir -= tam_kisim

    if tam_kisim == 1:
        mevcut_deger += 1 / (2 ** adim)

    adim += 1

print(f"0.1 sayısının binary karşılığı: {ikili_kesir}")
