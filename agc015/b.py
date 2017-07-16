def main():
    floors = input()

    count = 0

    for i in range(len(floors)):
        if floors[i] == 'U':
            count += (len(floors) - (i + 1)) + 2 * i
        else:
            count += 2 * (len(floors) - (i + 1)) + i

    print(count)


if __name__ == '__main__':
    main()
