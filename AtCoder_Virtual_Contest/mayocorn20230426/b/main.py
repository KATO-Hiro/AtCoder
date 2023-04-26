# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    print(n * (n - 1) // 2)


if __name__ == "__main__":
    main()
