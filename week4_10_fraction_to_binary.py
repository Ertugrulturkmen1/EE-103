# Kesirli sayıyı ikili (binary) sisteme çevirme
kesir = 0.375
ikili_kesir = "0."

while kesir > 0:
    kesir *= 2
    tam_kisim = int(kesir)
    ikili_kesir += str(tam_kisim)
    kesir -= tam_kisim

print(ikili_kesir)
