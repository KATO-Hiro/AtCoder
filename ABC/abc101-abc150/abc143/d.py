# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    n = int(input())
    l = sorted(list(map(int, input().split())))
    ans = 0

    # KeyInsight
    # a < b < c かつ a + b < cとなる組み合わせ
    # 2つの値a, bを決め打ち
    # See:
    # https://www.youtube.com/watch?v=3U_N7zelnMM
    for i in range(n):
        for j in range(i + 1, n):
            ab = l[i] + l[j]
            right = bisect(l, ab - 1)
            left = j + 1
            ans += right - left

    print(ans)


if __name__ == '__main__':
    main()
