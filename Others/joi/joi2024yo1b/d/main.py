# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    n = int(input())
    count = 0

    while True:
        r = x % 3

        if r == 0:
            x += 1
        elif r == 1:
            x *= 2
        else:
            x *= 3

        count += 1

        if x >= n:
            break

    print(count)


if __name__ == "__main__":
    main()
