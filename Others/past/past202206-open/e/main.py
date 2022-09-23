# -*- coding: utf-8 -*-


def main():
    from math import ceil, sqrt
    import sys

    input = sys.stdin.readline

    n = int(input())
    # i回目の操作による項数の合計 = i ** 2個

    # nが何回目の操作に含まれるかを調べる
    j = ceil(sqrt(n))
    n -= (j - 1) ** 2

    # 上記の操作のうち、どこに位置するかを調べる
    if n < j:
        print(j - n + 1)
    else:
        print(n - j + 1)


if __name__ == "__main__":
    main()
