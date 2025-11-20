# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        if i <= m:
            print("OK")
        else:
            print("Too Many Requests")


if __name__ == "__main__":
    main()
