# -*- coding: utf-8 -*-


def main():
    s = input()
    a, b, c, d = list(map(int, input().split()))

    # See:
    # https://beta.atcoder.jp/contests/arc049/submissions/1406025
    q = '"'
    print(s[:a] + q + s[a:b] + q + s[b:c] + q + s[c:d] + q + s[d:])


if __name__ == '__main__':
    main()
