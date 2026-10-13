# Kullanıcıdan bir tam sayı alıyoruz
given_number = int(input("Karekökü bulunacak bir tam sayı girin: "))

# Negatif sayı kontrolü (c şıkkı)
if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    # Tahmine 1'den başlıyoruz (a şıkkı)
    guess = 1
    
    # Tahminin karesi, girilen sayıdan küçük olduğu sürece tahmini 1 artırıyoruz
    while guess**2 < given_number:
        guess += 1
        
    # Döngü bittikten sonra eşitlik sağlanıp sağlanmadığını kontrol ediyoruz (b şıkkı)
    if guess**2 == given_number:
        print(f"{given_number} sayısının karekökü: {guess}")
    else:
        print(f"{given_number} bir tam kare sayı değildir.")