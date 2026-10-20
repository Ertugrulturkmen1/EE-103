# 5. Benzersiz karakter sayısı
s = "abcabc"
benzersiz_harfler = ""

for harf in s:
    if harf not in benzersiz_harfler:
        benzersiz_harfler += harf

print(len(benzersiz_harfler))
