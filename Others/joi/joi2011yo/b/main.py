# -*- coding: utf-8 -*-


def main():
    s = input()
    n = int(input())
    ans = 0

    # See:
    # https://atcoder.jp/contests/joi2011yo/submissions/1333209
    for i in range(n):
        # KeyInsight:
        # 文字列が短いので、単純に2倍すればいい
        # 先頭と末尾に関係する問題で、文字の長さが短い場合は2個分を並べる
        t = input() * 2

        if s in t:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
