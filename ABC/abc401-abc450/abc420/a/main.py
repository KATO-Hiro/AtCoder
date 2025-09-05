# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    z = x + y

    if z > 12:
        z -= 12

    print(z)


if __name__ == "__main__":
    main()
