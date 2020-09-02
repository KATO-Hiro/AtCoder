# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    max_a = 10 ** 6
    numbers = [0 for _ in range(max_a + 1)]

    # KeyInsight:
    # 調和級数: 計算量 O(AlogA)
    # ◯: 素因数分解をすればよいことには気がつけた。
    # △: 4ケースWA・TLEが取れず
    for ai in a:
        numbers[ai] += 1

    is_pairwise = True

    # 素因数の判定
    # 素因数の倍数の要素を数えている
    for i in range(2, max_a + 1):
        count = 0

        for j in range(i, max_a + 1, i):
            count += numbers[j]

            # 2つ以上ある数の倍数があった場合は、少なくともpairwiseではない
            if count > 1:
                is_pairwise = False

    if is_pairwise:
        print("pairwise coprime")
        exit()

    value_gcd = 0

    # 全ての要素のGCDが1かどうかを判定
    for i in range(n):
        value_gcd = gcd(value_gcd, a[i])

        if value_gcd == 1:
            print("setwise coprime")
            exit()

    print("not coprime")


if __name__ == '__main__':
    main()
