# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    pattern_count = 0

    # KeyInsight
    # 3つの数字a, b, cとして，場合分け
    # a = b = c
    pattern_count += 1

    # a <= b < c
    pattern_count += (n - k) * 3

    # a < b <= c
    pattern_count += (k - 1) * 3

    # a < b < c
    pattern_count += (n - k) * (k - 1) * 6

    print(pattern_count / (n ** 3))


if __name__ == '__main__':
    main()
