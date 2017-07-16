import sys

import math


def main():
    n, m = map(int, input().split())

    diff = abs(n - m)

    if diff > 1:
        print(0)
        return 0

    if diff == 1:
        print(math.factorial(n) * math.factorial(m) % (10 ** 9 + 7))
    else:
        print(math.factorial(n) * math.factorial(m) * 2 % (10 ** 9 + 7))

    return 0


if __name__ == '__main__':
    sys.exit(main())
