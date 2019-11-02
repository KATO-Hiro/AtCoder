# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left

    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    now = 0
    count = 0

    # 出発時間と到着時間をそれぞれ計算して，二分探索
    # See:
    # https://atcoder.jp/contests/abc030/submissions/1126006
    while True:
        i = bisect_left(a, now)
        if i == n: break
        now = a[i] + x

        j = bisect_left(b, now)
        if j == m: break
        now = b[j] + y

        count += 1

    print(count)


if __name__ == '__main__':
    main()
