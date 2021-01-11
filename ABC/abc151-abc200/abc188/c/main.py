# -*- coding: utf-8 -*-


def main():
    from collections import deque

    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = deque()

    for ai in a:
        d.append(ai)

    while len(d) > 2:
        di = d.popleft()
        dj = d.popleft()

        d.append(max(di, dj))

    index = a.index(min(d))  # 0-index
    print(index + 1)


if __name__ == "__main__":
    main()
