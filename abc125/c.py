# -*- coding: utf-8 -*-


def main():
    from fractions import gcd

    n = int(input())
    a = list(map(int, input().split()))
    left = [0 for _ in range(n + 1)]
    right = [0 for _ in range(n + 1)]

    # KeyInsight
    # 一つを書き換える→消すと同じ意味
    # 最大公約数の交換則
    # 左右から最大公約数を前計算
    # See:
    # https://www.youtube.com/watch?v=8lm8o8L9Bmw
    # http://drken1215.hatenablog.com/entry/2019/04/27/224100_1
    for i in range(n):
        left[i + 1] = gcd(left[i], a[i])

    for i in range(n - 1, -1, -1):
        right[i] = gcd(right[i + 1], a[i])

    ans = 0

    for i in range(n):
        l = left[i]
        r = right[i + 1]
        ans = max(ans, gcd(l, r))

    print(ans)


if __name__ == '__main__':
    main()
