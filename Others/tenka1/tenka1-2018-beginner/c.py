# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted([int(input()) for _ in range(n)], reverse=True)
    ans = 0
    center = n // 2

    # See:
    # http://drken1215.hatenablog.com/entry/2018/10/28/222800
    # KeyInsight
    # a > b < c > d < e ...
    # a < b > c < d > e ...の形で決め打ちしてよい
    # それぞれの係数に着目する
    if n % 2 == 0:
        ans += sum(a[:center - 1]) * 2
        ans += a[center - 1]
        ans -= a[center]
        ans -= sum(a[center + 1:]) * 2
    else:
        ans1 = 0
        ans1 += sum(a[:center - 1]) * 2
        ans1 += a[center - 1]
        ans1 += a[center]
        ans1 -= sum(a[center + 1:]) * 2

        ans2 = 0
        ans2 += sum(a[:center]) * 2
        ans2 -= a[center]
        ans2 -= a[center + 1]
        ans2 -= sum(a[center + 2:]) * 2
        ans = max(ans1, ans2)

    print(ans)


if __name__ == '__main__':
    main()
