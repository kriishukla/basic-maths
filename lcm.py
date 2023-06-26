def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = 12
b = 15
print(a*b/gcd(a, b))
