# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))

    # See:
    # https://beta.atcoder.jp/contests/chokudai_S001/submissions/3108858
    print(*a)


if __name__ == '__main__':
    main()
