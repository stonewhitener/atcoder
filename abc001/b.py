m = int(input())

vv = 0

if 100 <= m <= 5000:
    vv = m * 10 // 1000
elif 6000 <= m <= 30000:
    vv = m // 1000 + 50
elif 35000 <= m <= 70000:
    vv = (m // 1000 - 30) // 5 + 80
elif m > 70000:
    vv = 89

print(str(vv).zfill(2))
