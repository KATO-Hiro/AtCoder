# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    a, b = map(int, input().split())
    first = s[a - 1]
    second = s[b - 1]
    t = list(s)
    t[a - 1] = second
    t[b - 1] = first

    print(''.join(t))


if __name__ == "__main__":
    main()
