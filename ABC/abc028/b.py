# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    s = input()

    # See:
    # https://beta.atcoder.jp/contests/abc028/submissions/1915254
    values = [s.count(si) for si in 'ABCDEF']
    print(' '.join(map(str, values)))


if __name__ == '__main__':
    main()
