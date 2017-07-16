s = input()
t = input()

for a, b in zip(s, t):
    if a != b:
        if a == '@' and b in ('a', 't', 'c', 'o', 'd', 'e', 'r'):
            continue
        if b == '@' and a in ('a', 't', 'c', 'o', 'd', 'e', 'r'):
            continue
        print('You will lose')
        break
else:
    print('You can win')
