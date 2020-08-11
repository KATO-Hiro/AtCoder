# -*- coding: utf-8 -*-


def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = float('inf')

    # KeyInsight:
    # xの座標の最小値から最大値までを探索すればよい
    # See: https://img.atcoder.jp/abc156/editorial.pdf
    left = min(x)
    right = max(x)

    for p in range(left, right + 1):
        summed = 0

        for xi in x:
            summed += (xi - p) ** 2

        ans = min(ans, summed)

    print(ans)


if __name__ == '__main__':
    main()
