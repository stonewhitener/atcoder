N, M, Q = map(int, input().split())
 
x = [[0 for j in range(N + 1)] for i in range(N + 1)]
 
for _ in range(M):
    L, R = map(int, input().split())
    x[L][R] += 1
 
for i in range(1, N + 1):
    for j in range(1, N + 1):
        x[i][j] += x[i][j - 1]
 
for j in range(1, N + 1):
    for i in reversed(range(1, N + 1)):
        x[i - 1][j] += x[i][j]
 
for _ in range(Q):
    p, q = map(int, input().split())
    print(x[p][q])
