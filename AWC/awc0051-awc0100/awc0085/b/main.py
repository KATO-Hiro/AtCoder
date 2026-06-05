# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    candidate = sum(a[:k])
    ans = candidate

    for i in range(k, n):
        candidate -= a[i - k]
        candidate += a[i]
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
