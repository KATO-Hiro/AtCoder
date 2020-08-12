# -*- coding: utf-8 -*-


def main():
    n = int(input())
    h = list(map(int, input().split()))
    cost = [0 for _ in range(n)]
    cost[1] = abs(h[1] - h[0])

    for i in range(2, n):
        cost[i] = min(cost[i - 2] + abs(h[i] - h[i - 2]),
                      cost[i - 1] + abs(h[i] - h[i - 1]))

    print(cost[n - 1])


if __name__ == '__main__':
    main()
