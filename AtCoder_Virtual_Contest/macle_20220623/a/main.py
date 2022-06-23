# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    n %= k

    print(min(n, abs(n - k)))


if __name__ == "__main__":
    main()
