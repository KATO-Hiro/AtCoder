# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    s = list(input().rstrip())[::-1]

    for i in range(n):
        si = s[i]

        if si == "@" and d >= 1:
            s[i] = "."
            d -= 1

    print("".join(s[::-1]))


if __name__ == "__main__":
    main()
