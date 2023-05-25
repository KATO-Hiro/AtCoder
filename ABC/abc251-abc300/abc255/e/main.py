# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    x = list(map(int, input().split()))
    freq = defaultdict(int)

    # ⚪︎: A1を決めると、残りの項も一意に決まる
    # △: 初項を変数yで置く、他の項は一次式で表現できる
    # △: 上記の数式からラッキーナンバーとなるために必要な値を逆算
    # c + by = xi、(b = -1か1)
    # y = (xi - c) // b
    b, c = 1, 0

    for i in range(n):
        for xi in x:
            freq[(xi - c) // b] += 1

        if i == n - 1:
            break

        b *= -1
        c = s[i] - c

    # △: xが一意であることから、上記の頻度 = 求める答え
    print(max(freq.values()))


if __name__ == "__main__":
    main()
