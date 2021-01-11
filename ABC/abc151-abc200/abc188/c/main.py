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

        if di > dj:
            d.append(di)
        else:
            d.append(dj)

    semi = min(d)

    for i in range(2 ** n):
        if a[i] == semi:
            print(i + 1)
            exit()


if __name__ == "__main__":
    main()
