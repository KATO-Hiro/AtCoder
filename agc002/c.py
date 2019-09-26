# -*- coding: utf-8 -*-


def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    # KeyInsight
    # 最後から直前の状態を考える
    # ある位置a[i]と右隣の値a[i+1]の和がL以上であれば構成できる
    # iの位置を特定
    # 左右の両端から切る
    pos = -1

    for i in range(n - 1):
        if (a[i] + a[i + 1]) >= l:
            pos = i

    if pos == -1:
        print("Impossible")
    else:
        print("Possible")

        # 1-indexに
        pos += 1

        # See:
        # https://atcoder.jp/contests/agc002/submissions/7179969
        ans = [i for i in range(1, pos)] + [i for i in range(n - 1, pos, -1)] + [pos]
        print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
