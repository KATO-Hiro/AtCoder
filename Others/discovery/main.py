# -*- coding: utf-8 -*-


def main():
    n = int(input())
    money = [100000, 50000, 30000, 20000, 10000]
    ids = [int(input()) for _ in range(n)]
    ans = [0 for _ in range(n)]

    # See:
    # https://atcoder.jp/contests/discovery2016-final/submissions/2303121
    for i, m in zip(ids, money):
        ans[i - 1] = m

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
