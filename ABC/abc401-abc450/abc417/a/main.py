# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    s = list(input().rstrip())

    for _ in range(b):
        s.pop()

    s = s[::-1]

    for _ in range(a):
        s.pop()

    print("".join(s[::-1]))


if __name__ == "__main__":
    main()
