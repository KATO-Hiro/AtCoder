# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    d = list(map(int, input().split()))
    week = a + b
    days = list()

    for di in d:
        di = di % week
        days.append(di)
        days.append(di + week)  # 環を数直線上で処理するときは2周分を持つ

    days = sorted(days)

    # 言い換え: 隣り合う予定2つに平日全てがおさまるか?
    for first, second in pairwise(days):
        if second - first > b:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
