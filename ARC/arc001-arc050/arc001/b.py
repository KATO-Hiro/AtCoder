# -*- coding: utf-8 -*-


def main():
    from collections import deque

    a, b = map(int, input().split())

    # BFS
    # See:
    # https://atcoder.jp/contests/arc001/submissions/7649526
    d = deque()
    # Initialize
    d.append((a, 0))

    while True:
        value, count = d.popleft()

        if value == b:
            print(count)
            exit()

        for i in [-10, -5, -1, 1, 5, 10]:
            d.append((value + i, count + 1))


if __name__ == '__main__':
    main()
