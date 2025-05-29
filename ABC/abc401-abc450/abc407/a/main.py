# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    for x in range(10**4):
        small = b * x
        large = b * (x + 1)

        if small <= a <= large:
            if (a - small) < (large - a):
                print(x)
            else:
                print(x + 1)

            exit()


if __name__ == "__main__":
    main()
