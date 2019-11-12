# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = -float('inf')

    # See:
    # https://www.slideshare.net/chokudai/abc031
    for first in range(n):
        # aに負の値があるため，0で初期化するとマズい
        # See:
        # https://atcoder.jp/contests/abc031/submissions/2336454
        t_score = -float('inf')
        a_score = -float('inf')

        for second in range(n):
            if first == second:
                continue

            if first < second:
                small = first
                large = second
            else:
                small = second
                large = first

            b = a[small:large + 1]
            takahashi_score = sum(b[::2])
            aoki_score = sum(b[1::2])

            # 青木君が選択する要素：丸を付けられ中で，最も得点が得られる要素を選択
            if aoki_score > a_score:
                a_score = aoki_score
                t_score = takahashi_score

        ans = max(ans, t_score)

    print(ans)


if __name__ == '__main__':
    main()
