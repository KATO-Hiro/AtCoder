# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 2変数のうち片方を固定、もう片方を高速化
    # Aiが単調増加
    # 尺取り法
    i, j = 0, 0
    ans = 0

    for i, ai in enumerate(a):
        while j < n and a[j] - ai <= k:
            j += 1

        ans += j - i - 1

    print(ans)


if __name__ == "__main__":
    main()
