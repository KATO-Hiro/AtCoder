# -*- coding: utf-8 -*-


def main():
    from math import ceil

    s = list(input())
    ans = [0 for _ in range(len(s))]

    # KeyInsight
    # 1. RLとなる部分に子どもたちが集まる
    # 2. 試行回数が偶数、かつ、最初の位置から偶奇が入れ替わることはない
    # See:
    # https://www.youtube.com/watch?v=lyHk98daDJo
    for i in range(2):
        count = 0

        # Rのみカウント
        for index, si in enumerate(s):
            if si == 'R':
                count += 1
            else:
                # R側の個数は切り上げ、L側の個数は切り捨て
                ans[index] += count // 2
                ans[index - 1] += ceil(count / 2)
                count = 0

        # 実装を楽にするため、入力と結果を反転させている&LRを入れ替え
        s = s[::-1]
        ans = ans[::-1]

        for index, si in enumerate(s):
            if si == 'L':
                s[index] = 'R'
            else:
                s[index] = 'L'

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
