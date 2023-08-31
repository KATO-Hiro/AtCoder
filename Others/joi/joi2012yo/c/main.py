# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a, b = map(int, input().split())
    c = int(input())
    d = [int(input()) for _ in range(n)]
    cal = c
    cost = a
    ans = cal // cost

    # コストが同じなので、カロリーの高いものから順に選ぶと1ドルあたりのカロリーを高くできる
    for di in sorted(d, reverse=True):
        cal += di
        cost += b

        ans = max(ans, cal // cost)

    print(ans)


if __name__ == "__main__":
    main()
