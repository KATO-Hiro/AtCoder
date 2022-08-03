# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p = map(int, input().split())
    mod = 10 ** 9 + 7

    # 小さなサンプルを試す
    # 条件を満たすものだけ数える
    # 規則性を見つける
    ans = ((p - 1) * pow(p - 2, n - 1, mod)) % mod
    print(ans)


if __name__ == "__main__":
    main()
