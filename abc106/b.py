def sieve(n):
    """
    Sieve of Eratosthenes
    """
    s = [True for _ in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * 2, len(s), i):
                s[j] = False
    return (i for i in range(n + 1) if s[i] and i > 1)
 
 
def main():
    n = int(input())
    primes = sieve(n)
    c = 0
    for i in range(1, n + 1, 2):
        if i in primes:
            continue
        cp = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cp += 1
        if cp == 8:
            c += 1
    print(c)
 
 
if __name__ == '__main__':
    main()
