# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    # See:
    # https://atcoder.jp/contests/past202004-open/submissions/12572191
    s = Counter(input())
    print(s.most_common()[0][0])


if __name__ == '__main__':
    main()
