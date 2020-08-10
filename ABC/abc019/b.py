# -*- coding: utf-8 -*-


def main():
    from itertools import groupby

    s = input()
    ans = ''

    # See:
    # https://docs.python.jp/3/library/itertools.html#itertools.groupby
    # https://beta.atcoder.jp/contests/abc019/submissions/3002673
    for key, group in groupby(s):
        ans += key + str(len(list(group)))

    print(ans)


if __name__ == '__main__':
    main()
