from collections import deque

n = int(input())
a = list(map(int, input().split()))

b = deque()

for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])

if len(a) % 2 == 1:
    b.reverse()

print(' '.join(map(str, b)))
