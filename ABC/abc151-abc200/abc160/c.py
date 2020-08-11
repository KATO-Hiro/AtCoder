# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    ans = a[-1] - a[0]

    for i in range(n):
        if (i + 1) < n:
            dist = a[i] + (k - a[i + 1])
            ans = min(ans, dist)

    print(ans)


if __name__ == '__main__':
    main()
