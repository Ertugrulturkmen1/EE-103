# 3. Ondalık Sayılarla Kullanıcı Girdisi ve Temel Aritmetik
this_year = str(2026)
first_two = float(this_year[:2])  # '20'
last_two = float(this_year[2:])  # '26'

mysum = first_two + last_two
print(f"{mysum:.2f}")

if mysum == 46:
    print("Correct")
else:
    print("Wrong")
