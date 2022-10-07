# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ans = 0

    # bを固定して考える
    for b in range(1, n + 1):
        # 0 % b, 1 % b, ..., n % b
        # = 0, 1, ..., b - 1, 0, 1, ..., b - 1, 0, 1, ..., r
        # n = p * b + q
        # 1サイクルに含まれる個数を数える
        p, q = divmod(n, b)
        ans += max(b - k, 0) * p

        # 端数を考える
        ans += max(q - k + 1, 0)
    
    # 例外処理
    if k == 0:
        ans -= n
    
    print(ans)


if __name__ == "__main__":
    main()
