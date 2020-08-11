# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split())) + [-1]
    i = 0  # 現在見ている数列aの位置
    ans = 0

    # KeyInsight
    # 尺取り法
    # See:
    # https://atcoder.jp/contests/abc038/submissions/744050
    while i < n:
        j = 1  # 単調増加する個数

        while a[i + 1] > a[i]:
            i += 1
            j += 1

        ans += j * (j + 1) // 2
        i += 1

    print(ans)


if __name__ == '__main__':
    main()
