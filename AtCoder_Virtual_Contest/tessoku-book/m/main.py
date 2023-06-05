# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 2変数のうち片方を固定、もう片方を高速化
    # Aiが単調増加
    # 尺取り法
    left = 0
    ans = 0

    # 右端を全探索
    # See:
    # https://atcoder.jp/contests/tessoku-book/submissions/34897506
    for right, ai in enumerate(a):
        while left < n and ai - a[left] > k:
            left += 1

        ans += right - left

    print(ans)


if __name__ == "__main__":
    main()
