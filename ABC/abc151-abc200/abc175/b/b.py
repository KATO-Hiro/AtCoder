# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys
    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))
    comb = list(combinations(range(n), 3))
    ans = 0

    for i, j, k in comb:
        a = l[i]
        b = l[j]
        c = l[k]

        # 3変数のうち、最大値が残りの2変数よりも大きいことを楽に実装する
        # See:
        # https://www.youtube.com/watch?v=auQRcs5JMwE&feature=youtu.be
        # a + b <= c (ただし、a < b < c)
        # 両辺にcを足す
        # a + b + c <= c + c
        if a == b:
            continue
        if b == c:
            continue
        if c == a:
            continue

        if sum([a, b, c]) <= 2 * max(a, b, c):
            continue

        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
