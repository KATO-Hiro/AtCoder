# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, p = map(int, input().split())
    pairs = list()

    for i in range(1, (10 ** 6) + 1):
        if p % i == 0:
            pairs.append((i, p // i))

    for n, m in pairs:
        if n + m == s:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
