# -*- coding: utf-8 -*-


def main():
    import sys
    from statistics import median

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ps = list()

    # 1の位置を取得
    for i, si in enumerate(s):
        if si == "1":
            ps.append(i)

    # pj - j: 左から見たときの1の個数を除くことで、数直線上の1箇所に集める問題と言い換えられる
    # この場合、中央値が最適解になる
    for j, pj in enumerate(ps):
        ps[j] = pj - j

    m = int(median(ps))
    ans = 0

    for pj in ps:
        ans += abs(pj - m)

    print(ans)


if __name__ == "__main__":
    main()
