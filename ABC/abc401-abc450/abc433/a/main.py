# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())

    for alpha in range(10**6 + 1):
        if x + alpha == (y + alpha) * z:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
