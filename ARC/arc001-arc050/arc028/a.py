# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    mod = n % (a + b)

    # See:
    # https://beta.atcoder.jp/contests/arc028/submissions/1678588
    if 0 < mod <= a:
        print('Ant')
    else:
        print('Bug')


if __name__ == '__main__':
    main()
