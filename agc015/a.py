def main():
    n, a, b = map(int, input().split())

    if a > b or (n == 1 and a != b):
        print(0)
    else:
        print((n - 1) * (b - a) - (b - a - 1))


if __name__ == '__main__':
    main()
