# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = min(a)

    # KeyInsight:
    # n = 2のケースで試す & 拡張する
    # 直感で全体のgcdという気がしたが、証明せずにsubmitしてしまった。
    for ai in a:
        ans = gcd(ans, ai)

    print(ans)


if __name__ == "__main__":
    main()
