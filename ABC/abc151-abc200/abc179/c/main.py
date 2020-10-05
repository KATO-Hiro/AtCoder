# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    ans = 0

    # KeyInsight:
    # 変数を一つ固定
    # 式を性質を保持しながら、単純化する
    for a in range(1, n):
        # a * b <= n - 1
        ans += (n - 1) // a

    print(ans)


if __name__ == '__main__':
    main()
