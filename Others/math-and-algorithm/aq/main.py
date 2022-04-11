# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    print(pow(a, b, mod))


if __name__ == "__main__":
    main()
