# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d = dict()
    pairs = list()

    # See:
    # https://www.youtube.com/watch?v=UTVg7wzMWQc&feature=youtu.be
    # KeyInsight:
    # 1〜Nまでの整数について、先頭と末尾の数字のペアをカウントする
    # ex: (1, 9), (9, 1)
    # (x, y)に対応する(y, x)の個数を加算する
    for i in range(1, n + 1):
        s = str(i)
        first = s[0]
        second = s[-1]
        pairs.append((first, second))

        if (first, second) not in d.keys():
            d[(first, second)] = 1
        else:
            d[(first, second)] += 1

    ans = 0

    for first, second in pairs:
        if (second, first) in d.keys():
            ans += d[(second, first)]

    print(ans)


if __name__ == '__main__':
    main()
