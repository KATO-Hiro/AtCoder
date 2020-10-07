# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    mod = 10 ** 9 + 7

    # See:
    # https://www.youtube.com/watch?v=yLkJZXkB6D0&feature=youtu.be
    # KeyInsight:
    # 包除原理

    # ◯
    # 全体 - 余事象
    # nの小さい値で愚直に数えようとした

    # △
    # 条件を丁寧に整理する、ベン図を活用する
    # 全体: 10 ^ n
    # 0を含まない: 9 ^ n
    # 9を含まない: 9 ^ n
    # 0, 9を含まない: 8 ^ n
    # 0, 9のうち少なくとも片方は含まない: 9 ^ n + 9 ^ n - 8 ^ n
    ans = pow(10, n, mod)
    ans -= pow(9, n, mod)
    ans -= pow(9, n, mod)
    ans += pow(8, n, mod)

    print(ans % mod)


if __name__ == '__main__':
    main()
