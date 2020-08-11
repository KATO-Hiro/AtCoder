# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cost = [0 for _ in range(n)]

    # See:
    # http://abc040.contest.atcoder.jp/data/abc/040/editorial.pdf
    # https://atcoder.jp/contests/abc040/submissions/1140205
    cost[1] = abs(a[1] - a[0])

    for i in range(2, n):
        candidate1 = cost[i - 1] + abs(a[i - 1] - a[i])
        candidate2 = cost[i - 2] + abs(a[i - 2] - a[i])
        cost[i] = min(candidate1, candidate2)

    print(cost[n - 1])


if __name__ == '__main__':
    main()
