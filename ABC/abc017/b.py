# -*- coding: utf-8 -*-


def main():
    from re import fullmatch
    x = input()

    # See:
    # https://beta.atcoder.jp/contests/abc017/submissions/2788653
    if fullmatch('(ch|[oku])*', x):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
