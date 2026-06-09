# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ri_max = 0
    ans = 0

    for _ in range(n):
        ti, ri = map(int, input().split())
        ans += ti + ri
        ri_max = max(ri_max, ri)

    ans -= ri_max
    print(ans)


if __name__ == "__main__":
    main()
