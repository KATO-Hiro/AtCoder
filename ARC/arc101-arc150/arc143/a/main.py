# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = sorted(map(int, input().split()))
    k = c

    # 操作の言い換え
    # 1つ目の操作 = 2つ目の操作 + 1
    # 全て同じ整数にするには、k回操作が必要
    # a <= b <= cで並び替え
    # k = cとしたときに、(k - a) + (k - b) <= kならc、それ以外は-1

    if (k - a) + (k - b) <= k:
        print(c)
    else:
        print(-1)


if __name__ == "__main__":
    main()
