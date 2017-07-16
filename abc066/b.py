s = input()

s = s[:-1]

if len(s) % 2 != 0:
    s = s[:-1]

while True:
    if s[:len(s) // 2] == s[len(s) // 2:]:
        break
    else:
        s = s[:-2]

print(len(s))
