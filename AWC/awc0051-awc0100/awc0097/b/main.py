# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    t = list(map(int, input().split()))
    ans = sum(t[:k])
    candidate = ans

    for i in range(k, n):
        candidate += t[i]
        candidate -= t[i - k]
        ans = max(ans, candidate)

    ans *= 1000
    ans //= k
    print(ans)


if __name__ == "__main__":
    main()
