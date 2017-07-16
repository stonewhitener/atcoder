import sys


def main():
    x, a, b = map(int, input().split())

    if -a + b <= x:
        if -a + b <= 0:
            print('delicious')
        else:
            print('safe')
    else:
        print('dangerous')

    return 0


if __name__ == '__main__':
    sys.exit(main())
