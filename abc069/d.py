# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    ans = [[0 for _ in range(w)] for _ in range(h)]

    # 一筆書きの要領で，a[i]の数だけ数字を順番に埋めていく
    for hi in range(h):
        for wi in range(w):
            if a[i] == 0:
                i += 1

            ans[hi][wi] = i + 1
            a[i] -= 1

    # 出力のときに，奇数番目の行(0-index)だけ反転させる
    for index, a in enumerate(ans):
        if index % 2 == 1:
            a = a[::-1]

        print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()
