# -*- coding: utf-8 -*-


def solve():
    n, w = map(int, input().split())
    c = list(map(int, input().split()))
    w2 = w * 2
    costs = [0] * w2

    for i, ci in enumerate(c):
        costs[i % w2] += ci

    costs = costs + costs
    base = sum(costs[:w])
    ans = base

    for i in range(1, w2):
        candidate = base
        candidate -= costs[i - 1]
        candidate += costs[i + w - 1]

        ans = min(ans, candidate)
        base = candidate

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
