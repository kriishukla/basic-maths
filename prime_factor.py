def print_prime_factors(n):
    if n <= 1:
        return

    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2

    while n % 3 == 0:
        print(3, end=" ")
        n = n // 3

    i = 5
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n = n // i

        while n % (i + 2) == 0:
            print(i + 2, end=" ")
            n = n // (i + 2)

        i = i + 6

    if n > 3:
        print(n, end=" ")

    print()

n = 450
print_prime_factors(n)
