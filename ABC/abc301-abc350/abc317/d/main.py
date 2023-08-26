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

    # dp[i][j]: i番目の選挙区でj議席を獲得するのに必要な鞍替えの人数
    # j: 議席数とすべきところを選挙区としていたのが敗因
    inf = 10**18
    seat_sum = sum(seats) // 2 + 1
    size = seat_sum + 1
    dp = [inf] * size
    dp[0] = 0

    for i, (cost, seat) in enumerate(zip(costs, seats)):
        for j in range(size)[::-1]:
            nj = min(seat_sum, j + seat)
            dp[nj] = min(dp[nj], dp[j] + cost)

    print(dp[seat_sum])


if __name__ == "__main__":
    main()
