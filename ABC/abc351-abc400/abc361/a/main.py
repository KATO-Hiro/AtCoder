# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(k, x)

    print(*a)


if __name__ == "__main__":
    main()
