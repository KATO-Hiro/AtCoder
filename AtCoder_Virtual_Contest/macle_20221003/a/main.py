# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for i, bi in enumerate(b):
        c = min(bi, a[i])
        ans += c
        bi -= c

        c = min(bi, a[i + 1])
        ans += c
        a[i + 1] -= c

    print(ans)


if __name__ == "__main__":
    main()
