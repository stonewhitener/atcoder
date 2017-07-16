import math

a, b, k, l = map(int, input().split())

print(min((k // l) * b + (k % l) * a, math.ceil(k / l) * b))
