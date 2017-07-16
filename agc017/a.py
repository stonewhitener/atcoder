import math
 
 
def comb(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)
 
 
def main():
    n, p = map(int, input().split())
    a = tuple(map(lambda x: int(x) % 2, input().split()))
 
    if n == 1 and a[0] % 2 != p:
        print(0)
        return 0
 
    t = len(tuple(filter(lambda x: x == 1, a)))
    f = n - t
 
    f_comb = 0
    for j in range(f + 1):
        f_comb += comb(f, j)
 
    t_comb = 0
    if p == 0:
        for i in range(t + 1):
            if i % 2 == 0:
                t_comb += comb(t, i)
    else:
        for i in range(t + 1):
            if i % 2 == 1:
                t_comb += comb(t, i)
 
    print(int(t_comb * f_comb))
 
    return 0
 
 
if __name__ == '__main__':
    main()
