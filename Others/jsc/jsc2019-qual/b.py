# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0

    # See:
    # https://www.youtube.com/watch?v=JTH27weC38k
    # https://atcoder.jp/contests/jsc2019-qual/submissions/7107452

    # Key Insight
    # 2つの整数の順序対(i, j)の選び方
    # 同じブロックにある/異なるブロックにある で場合分け

    # 同じブロックにある
    # Bi > Bjとなる組み合わせを全探索
    for i in range(n - 1):
        count = 0

        for j in range(i + 1, n):
            if a[i] > a[j]:
                count += 1

        # 一つのブロックにある組み合わせのk倍
        ans += count * k
        ans %= mod

    # 別のブロックにある
    for i in range(n):
        count = 0

        for j in range(n):
            if a[i] > a[j]:
                count += 1

        # k個のブロックから2個選ぶ（kC2）
        ans += count * (k * (k - 1) // 2)
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
