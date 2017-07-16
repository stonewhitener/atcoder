n = int(input())
a = [int(x) for x in input().split()]
 
l = 0
r = sum(a)
 
d = 2 * 10 ** 9 + 1
 
for i in range(n - 1):
    l += a[i]
    r -= a[i]
    d = min(d, abs(l - r))
 
print(d)
