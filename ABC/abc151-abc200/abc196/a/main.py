# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ans = -1000

    for x in range(a, b + 1):
        for y in range(c, d + 1):
            ans = max(ans, x - y)

    print(ans)


if __name__ == "__main__":
    main()
