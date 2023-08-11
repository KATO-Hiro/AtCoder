# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = sorted(list(map(int, input().split())))
    m = n // 2
    mid1, mid2 = d[:m][-1], d[m:][0]
    ans = 0

    if mid1 != mid2:
        ans = mid2 - mid1

    # print(mid1, mid2)
    # print(d)
    print(ans)


if __name__ == "__main__":
    main()
