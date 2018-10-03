# -*- coding: utf-8 -*-


def main():
    n = int(input())
    seats = [0] * 100000
    count = 0

    for i in range(n):
        left, right = map(int, input().split())

        for j in range(left - 1, right):
            seats[j] = 1

    for seat in seats:
        if seat == 1:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
