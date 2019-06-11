# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cost = [float('inf') for _ in range(n)]
    cost[n - 1] = 0

    for j in range(2, n + 1):
        for i in range(max(1, j - k), j + 1):
            cost[n - j] = min(cost[n - j],
                              cost[n - i] + abs(h[n - i] - h[n - j]))

    print(cost[0])


if __name__ == '__main__':
    main()
