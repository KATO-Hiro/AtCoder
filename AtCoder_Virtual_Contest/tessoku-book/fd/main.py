# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    # パスグラフ + 両端の頂点を結ぶ
    print(n)

    for i in range(1, n):
        print(i, i + 1)

    print(n, 1)


if __name__ == "__main__":
    main()
