# -*- coding: utf-8 -*-


def solve():
    from collections import deque

    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = deque()

    for day, (ai, bi) in enumerate(zip(a, b), 1):
        for i in range(ai):
            q.append(day)

        for i in range(bi):
            q.popleft()

        while q and day - q[0] >= d:
            q.popleft()

    print(len(q))


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
