# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    d, n = map(int, input().split())
    count = 0

    for i in range(1, 110):
        value = 100**d * i
        tmp = value
        tmp_count = 0

        while tmp % 100 == 0:
            tmp //= 100
            tmp_count += 1

        if tmp_count != d:
            continue

        count += 1

        if count == n:
            print(value)
            exit()


if __name__ == "__main__":
    main()
