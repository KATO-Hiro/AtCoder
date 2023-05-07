# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())

    while len(s) > 0:
        t = s.pop()
        n = len(s)

        if s[:n // 2] == s[n // 2:]:
            print(n)
            exit()


if __name__ == "__main__":
    main()
