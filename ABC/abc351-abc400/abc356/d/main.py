# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = 0
    mod = 998244353

    # 各桁でkを2進数表記したときのビットが立っている個数を数える
    for i in range(60):
        # mのi番目のビットが立っているかどうか
        if not (m >> i & 1):
            continue

        # kを0から順番に並べると、0が2 ^ i個、1が2 ^ i個 (周期2 ^ (i + 1))並んでいる
        # 周期と端数を求める
        period = 1 << (i + 1)
        remain = n % period

        ans += (n - remain) // 2
        ans %= mod

        if remain >= (1 << i):
            ans += remain - (1 << i) + 1
            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
