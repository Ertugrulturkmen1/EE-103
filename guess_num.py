import secret_number
tahmin = 0
deneme_sayisi = 0

while tahmin != secret_number.secretNum:
    tahmin = int(input("Bir sayı tahmin edin: "))
    deneme_sayisi += 1  # Her tahminde deneme sayısını 1 artırıyoruz
    
    if tahmin < secret_number.secretNum:
        print("Tahmininiz çok düşük.")
    elif tahmin > secret_number.secretNum:
        print("Tahmininiz çok yüksek.")
    else:
        print("Tebrikler, gizli sayıyla aynı!")
        break  # Doğru bilirse döngüden çık
        
    # Eğer 5 deneme hakkı dolduysa ve tahmin hala yanlışsa:
    if deneme_sayisi == 5:
        # Sonsuz döngüye gir (Programı durdurmak için terminalde Ctrl + C yapmanız gerekir)
        while True:
            print("Oh! Noooooo...")