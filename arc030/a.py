# -*- coding: utf-8 -*-


def main():
    n = int(input())
    k = int(input())

    # KeyInsight
    # 閉路グラフは列を扱う問題の派生形
    if n // 2 >= k:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
