# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = sum(a[:k])
    ans = tmp

    for i in range(k, n):
        tmp += a[i]
        tmp -= a[i - k]

        ans = min(tmp, ans)

    print(ans)


if __name__ == "__main__":
    main()
