# -*- coding: utf-8 -*-


def main():
    k = int(input())
    ans = [0 for _ in range(k + 1)]
    ans[0] = 1
    ans[1] = 1

    for i in range(2, k + 1):
        ans[i] = ans[i - 1] + ans[i - 2]

    # KeyInsight
    # フィボナッチ数列と互除法との関係を結び付けられるか
    # See:
    # http://arc051.contest.atcoder.jp/data/arc/051/editorial.pdf
    print(ans[k - 1], ans[k])


if __name__ == '__main__':
    main()
