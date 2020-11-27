# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, p = map(int, input().split())

    for n in range(1, (10 ** 6) + 1):
        if p % n != 0:
            continue

        m = p // n

        if n + m == s:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
