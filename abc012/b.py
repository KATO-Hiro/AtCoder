# -*- coding: utf-8 -*-


def main():
    n = int(input())

    # See:
    # https://beta.atcoder.jp/contests/abc012/submissions/1352862
    hour = n // 3600
    minute = (n // 60) % 60
    second = n % 60
    print('{:02d}:{:02d}:{:02d}'.format(hour, minute, second))


if __name__ == '__main__':
    main()
