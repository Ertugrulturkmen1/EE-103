# Kullanıcıdan bir tam sayı alıyoruz
given_number = int(input("Küp kökü bulunacak bir tam sayı girin: "))

# Sayı negatif de olsa mantığın çalışması için tahmini 0'dan başlatıyoruz
guess = 0

# Girilen sayının mutlak değerine ulaşana kadar tahmini artırıyoruz
while guess**3 < abs(given_number):
    guess += 1

# Tahminin küpü sayının mutlak değerine eşit mi kontrol ediyoruz
if guess**3 == abs(given_number):
    # Eğer orijinal sayı negatifse, tahmini de negatif yapıyoruz
    if given_number < 0:
        guess = -guess
    print(f"{given_number} sayısının küp kökü: {guess}")
else:
    print(f"{given_number} mükemmel bir küp sayı değildir.")