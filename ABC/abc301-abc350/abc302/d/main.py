# -*- coding: utf-8 -*-


def main():
    import sys
    from bisect import bisect_left

    input = sys.stdin.readline

    n, m, d = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    ans = -1

    for ai in a:
        # ai + d以下となる最大値があるインデックス
        i = bisect_left(b, ai + d + 1) - 1
        bi = b[i]

        if i >= 0 and abs(ai - bi) <= d:
            ans = max(ans, ai + bi)

    print(ans)


if __name__ == "__main__":
    main()
