# -*- coding: utf-8 -*-


def main():
    a, k = list(map(int, input().split()))
    total = a
    day_count = 0

    if k == 0:
        print(2 * (10 ** 12) - a)
    else:
        while total < 2 * (10 ** 12):
            total += 1 + k * total
            day_count += 1

        print(day_count)


if __name__ == '__main__':
    main()
