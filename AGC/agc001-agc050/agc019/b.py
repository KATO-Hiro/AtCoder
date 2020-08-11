# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    from itertools import combinations

    a = Counter(input())
    ans = 1

    # KeyInsight
    # 何も操作しない場合が1通り
    # 異なる文字(a-z)を2つ選ぶ組み合わせ

    # 以下の場合だと，組み合わせは増えない．
    # 例2：abcda．1文字目と5文字目の場合，2文字目と4文字目の場合の並びは同じ．
    # See:
    # https://www.youtube.com/watch?v=9OiB8ot3a0w
    for i, j in combinations(a.values(), 2):
        ans += i * j

    print(ans)


if __name__ == '__main__':
    main()
