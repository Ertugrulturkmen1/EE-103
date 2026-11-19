year = int(input("What year is this?"))
sum = 0
for i in range(year):
    sum += int(i)

number_of_digits = len(str(year))   
result = sum / number_of_digits
print(f"The result is: {result}")
    
