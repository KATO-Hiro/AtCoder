# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = 998244353
    q = pow(n**2, mod - 2, mod)  # 1 / q
    q *= 2
    q %= mod

    # 確率を求めておき、最後に期待値に
    # 白いボールは区別できない = 確率が等しい + 黒いボールが左端にある確率から求められる
    p = 1

    for _ in range(k):
        p = p * (1 - q * (n - 1)) + (1 - p) * q
        p %= mod

    inv = pow(2, mod - 2, mod)
    ans = p + (1 - p) * (2 + n) * inv
    ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
