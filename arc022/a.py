# -*- coding: utf-8 -*-


def main():
    from re import search

    s = input().lower()

    # See:
    # https://beta.atcoder.jp/contests/arc022/submissions/1709214
    if search('.*i.*c.*t', s):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
