# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.readline

    n, q = map(int, input().split())
    d = defaultdict(int)

    for i in range(1, n + 1):
        d[i] = 1

    que = deque([i for i in range(1, n + 1)])

    for _ in range(q):
        xi, yi = map(int, input().split())
        count = 0

        while que[0] <= xi:
            qi = que.popleft()
            count += d[qi]
            d[yi] += d[qi]
            d[qi] = 0

        print(count)


if __name__ == "__main__":
    main()
