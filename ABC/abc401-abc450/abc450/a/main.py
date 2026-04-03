# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = [i for i in range(1, n + 1)][::-1]
    print(*ans, sep=",")


if __name__ == "__main__":
    main()
