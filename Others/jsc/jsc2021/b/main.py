# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    print(*sorted(a ^ b))


if __name__ == "__main__":
    main()
