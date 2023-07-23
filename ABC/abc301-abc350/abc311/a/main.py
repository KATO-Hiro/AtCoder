# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    ans = 0

    for alpha in "ABC":
        ans = max(ans, s.index(alpha))

    print(ans + 1)


if __name__ == "__main__":
    main()
