def sieve(n):
    if n <= 1:
        return

    isPrime = [True] * (n + 1)

    for i in range(2, int(n**0.5) + 1):
        if isPrime[i]:
            for j in range(2*i, n+1, i):
                isPrime[j] = False

    for i in range(2, n+1):
        if isPrime[i]:
            print(i, end=" ")

n = 18
sieve(n)
