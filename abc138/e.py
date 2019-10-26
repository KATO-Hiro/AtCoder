# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left

    s = input()
    t = input()
    n = len(s)
    m = len(t)
    alpha = [[] for _ in range(26)]

    # See:
    # https://www.youtube.com/watch?v=lWETOlGiuaI
    # KeyInsight
    # 部分列判定：場所i以降で文字Cが最初に現れる位置を高速に求める
    # アルファベットの出現位置をリストで記録

    # sで各文字が出現する位置を2周分記録
    for index, si in enumerate(s):
        alpha[(ord(si) - ord('a'))].append(index)

    for index, si in enumerate(s):
        alpha[(ord(si) - ord('a'))].append(index + n)

    ans = 0
    p = 0

    for ti in t:
        c = ord(ti) - ord('a')

        if len(alpha[c]) == 0:
            print('-1')
            exit()

        # 二分探索でWAを量産
        # See:
        # https://atcoder.jp/contests/abc138/submissions/6999265
        p = alpha[c][bisect_left(alpha[c], p)] + 1

        if p >= n:
            p -= n
            ans += n

    ans += p

    print(ans)


if __name__ == '__main__':
    main()
