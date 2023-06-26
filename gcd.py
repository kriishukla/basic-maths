def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = 12
b = 15
print(gcd(a, b))
# 21 17
# 17 4
# 13 4
# 9 4
# 5 4
# 1 4
# 3 1
# 2 1
# 1 1
