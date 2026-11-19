def is_even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
is_even_or_odd_alias = is_even_or_odd

print(is_even_or_odd(7))
print(is_even_or_odd_alias(7))

print(is_even_or_odd(10))
print(is_even_or_odd_alias(10))

print(is_even_or_odd_alias is is_even_or_odd)