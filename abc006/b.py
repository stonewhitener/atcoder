def tribonacci_generator():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, (a + b + c) % 10007

n = int(input())

i = tribonacci_generator()

for _ in range(n - 1):
    next(i)

print(next(i))
