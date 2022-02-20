# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    r = a.count(1)
    y = a.count(2)
    b = a.count(3)

    ans = r * (r - 1) // 2
    ans += y * (y - 1) // 2
    ans += b * (b - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
