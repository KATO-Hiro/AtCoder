# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate
    from operator import xor

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    s = list(accumulate(a, xor, initial=0))
    ans = 0

    # 累積和の考え方をベース、累積xorを取る
    # 差分は、s[r] xor s[l - 1]

    # bit演算では、桁ごとに独立して考えるのが定石
    # 合計に寄与するのは、xorが1となる場合のみ（片方が0で、もう片方が1のとき）
    # 各桁について、1となる個数 * (n + 1 - 1となる個数) * (2 ** k)の総和
    # ただし、区間の長さが1の場合を含んでいるため、最後に引く
    for digit in range(30):
        one_count = 0

        for si in s:
            if si >> digit & 1:
                one_count += 1

        ans += one_count * (n + 1 - one_count) * (2**digit)

    ans -= sum(a)

    print(ans)


if __name__ == "__main__":
    main()
