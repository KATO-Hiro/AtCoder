# -*- coding: utf-8 -*-


def main():
    import sys
    from math import isqrt

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    # 重複なく数えるには、標準形を定める
    # a = 1、2のみ考えればよい
    # a >= 3の場合は、bに押しつけることで上記と等価になる
    for a in range(1, 3):
        x = n

        for _ in range(a):
            x //= 2

        # 誤差に注意
        ans += isqrt(x)

    print(ans)


if __name__ == "__main__":
    main()
