# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    s = Counter(input())
    ans = 1
    mod = 10 ** 9 + 7

    # See:
    # https://www.youtube.com/watch?v=g2LMI15ha_U

    # Key Insight
    # 要素がすべて異なる=各要素が1個以下になるように選ぶ
    # それぞれの要素を独立に考えられる
    for index, count in s.items():
        # 選び方：ある文字の個数 + ある文字を選ばない(1通り)
        ans *= count + 1
        ans %= mod

    # すべての文字の積 - すべて選ばない(1通り)
    print(ans - 1)


if __name__ == '__main__':
    main()
