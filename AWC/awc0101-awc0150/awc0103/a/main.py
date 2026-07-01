# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    x = [int(input()) for _ in range(n)]
    k -= 1
    print(x[k] - 1)


if __name__ == "__main__":
    main()
