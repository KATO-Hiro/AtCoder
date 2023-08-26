# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    costs = [0] * n
    seats = [0] * n

    for i in range(n):
        xi, yi, zi = map(int, input().split())
        need = (xi + yi) // 2 + 1
        cost = max(0, need - xi)
        costs[i] = cost

        seats[i] = zi

    # print(costs)
    # print(seats)

    # dp[i][j]: i番目の選挙区でj議席を獲得するのに必要な鞍替えの人数
    # j: 議席数とすべきところを選挙区としていたのが敗因
    inf = 10**18
    size = 10**5 + 1
    dp = [inf] * size
    dp[0] = 0

    for i, (cost, seat) in enumerate(zip(costs, seats)):
        ndp = [inf] * size

        for j in range(size):
            if dp[j] == inf:
                continue

            ndp[j] = min(ndp[j], dp[j])
            nj = j + seat

            if nj <= size:
                ndp[nj] = min(ndp[nj], dp[j] + cost)

        dp = ndp

    # print(dp)
    at_least = sum(seats) // 2 + 1
    # print(at_least)
    print(min(dp[at_least:]))


if __name__ == "__main__":
    main()
