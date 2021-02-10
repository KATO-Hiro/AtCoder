# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    mod = 10 ** 9 + 7

    for i in range(5 * 10 ** 5):
        m = i * mod + z

        if (m % 17 == x) and (m % 107 == y):
            print(m)
            exit()


if __name__ == "__main__":
    main()
