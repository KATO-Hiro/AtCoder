# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for l in range(n):
        a_min = 10 ** 6

        for r in range(l, n):
            a_min = min(a_min, a[r])
            ans = max(ans, (r - l + 1) * a_min)

    print(ans)


if __name__ == "__main__":
    main()
