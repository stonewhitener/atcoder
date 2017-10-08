N, C = map(int, input().split())

L = [int(input()) for _ in range(N)]
L.sort(reverse=True)

count = 0
j = N - 1

for i in range(N):
    if i == j:
        count += 1

    if i >= j:
        break

    if L[i] + L[j] + 1 <= C:
        count += 1
        j -= 1
    else:
        count += 1

print(count)
