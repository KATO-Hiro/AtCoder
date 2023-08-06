# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))

    if n == 1:
        print(0)
    else:
        ans = max(0, max(p[1:]) - p[0] + 1)
        print(ans)


if __name__ == "__main__":
    main()
