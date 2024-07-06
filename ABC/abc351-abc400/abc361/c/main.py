# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    inf = 10**18
    ans = inf
    m = n - k

    for i in range(n):
        j = i + (m - 1)

        if j >= n:
            break

        ans = min(ans, a[j] - a[i])

    print(ans)


if __name__ == "__main__":
    main()
