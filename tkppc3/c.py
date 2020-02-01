# -*- coding: utf-8 -*-


def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    right = 0
    total_tmp = 1

    # KeyInsight: 数列の一部が条件を満たすかどうかを高速に判定する方法の一つが、尺取り法
    # See:
    # https://atcoder.jp/contests/tkppc3/submissions/3068446

    for left in range(n):
        # 左端から右に一つずつ伸ばす
        while right < n and total_tmp * a[right] < p:
            total_tmp *= a[right]
            right += 1

        # 条件に一致
        if right < n and total_tmp * a[right] == p:
            print('Yay!')
            exit()

        # 左端が右に一つずれるため、それに伴う処理
        total_tmp //= a[left]

    print(':(')


if __name__ == '__main__':
    main()
