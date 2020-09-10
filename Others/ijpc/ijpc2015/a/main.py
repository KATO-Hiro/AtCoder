# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    # KeyInsight:
    # N人が与えられた順番通りに並んでいるとは限らない = 並び替えても良い
    # 空席の数が少ない順にソートBi
    # N人の席
    ans = n
    # 両端の処理
    ans += a[0]
    ans += a[-1]

    # BiとBi+1のうち、大きい方を選択
    for first, second in zip(a, a[1:]):
        ans += max(first, second)

    print(ans)


if __name__ == '__main__':
    main()
