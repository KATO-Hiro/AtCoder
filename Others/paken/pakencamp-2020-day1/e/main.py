# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    if x > y:
        print(x, 2 * x + y)
    elif x < y:
        print(x + 2 * y, y)
    else:
        if x == y == 0:
            print(1, 1)
        else:
            print(-1)


if __name__ == "__main__":
    main()
