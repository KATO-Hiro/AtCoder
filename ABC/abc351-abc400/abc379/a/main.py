# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = list(input().rstrip())
    s = b + c + a
    t = c + a + b

    print(s, t)


if __name__ == "__main__":
    main()
