# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    n = int(input())
    plans = dict()
    fee = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        plans[bi] = ai

    sorted_plans = sorted(plans.items())

    for k in range(n - 1):
        fee.append(sorted_plans[k + 1][0] +
                   sorted_plans[k][1] - sorted_plans[k][0])

    m = int(input())
    t = [int(input()) for _ in range(m)]

    for x in range(m):
        index = bisect(fee, t[x])
        print(sorted_plans[index][0] + max(0, t[x] - sorted_plans[index][1]))


if __name__ == '__main__':
    main()
