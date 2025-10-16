# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    u, v = s[: n // 2], s[n // 2 + 1 :]
    print(u + v)


if __name__ == "__main__":
    main()
