# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a = sum(a)
    sum_b = sum(b)
    operation_count = sum_b - sum_a

    # 数列bの合計は数列aの合計よりも大きい必要がある
    if operation_count >= 0:
        # KeyInsight
        # https://img.atcoder.jp/apc001/editorial.pdf
        # 条件を満たすために，少なくとも何回操作が必要か?
        # ai < biのとき少なくとも[(bi - ai) / 2]回，+2する必要がある
        # ai > biのとき少なくともai - bi回，+1する必要がある
        # 操作回数より大きくなければYes
        two_count = 0
        one_count = 0

        for ai, bi in zip(a, b):
            if ai > bi:
                one_count += ai - bi
            elif ai < bi:
                two_count += ceil((bi - ai) / 2)

        if one_count <= operation_count and two_count <= operation_count:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    main()
