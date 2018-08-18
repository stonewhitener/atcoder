s = input()
k = int(input())
 
for i in range(k):
    if s[i] == '1':
        continue
    else:
        print(s[i])
        break
else:
    print(1)
