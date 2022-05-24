# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(accumulate(a))
    ans = 0

    for i in range(n):
        ans += b[n - 1] - b[i]
        ans -= a[i] * (n - i - 1)

    print(ans)


if __name__ == "__main__":
    main()
