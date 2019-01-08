# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cost = [0 for _ in range(n)]

    for i in range(1, n):
        candidate1 = cost[i - 1] + abs(a[i - 1] - a[i])

        if i >= 2:
            candidate2 = cost[i - 2] + abs(a[i - 2] - a[i])
        else:
            candidate2 = float('inf')

        cost[i] = min(candidate1, candidate2)

    print(cost[n - 1])


if __name__ == '__main__':
    main()
