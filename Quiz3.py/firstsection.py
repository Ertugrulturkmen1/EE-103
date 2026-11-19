n = int(input("Enter n: "))
total = 0.0
for i in range(n):
    total += 0.1

print(f"total: {total}")
print(f"Equal: {total == n/10}")
print(f"Close enough: {abs(total - n/10) < 1e-9}")