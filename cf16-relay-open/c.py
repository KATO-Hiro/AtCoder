# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n = int(input())
    d = deque()

    for i in range(2 ** n):
        d.append(int(input()))

    while len(d) >= 2:
        x = d.popleft()
        y = d.popleft()
        winner = abs(x - y)
        d.append(winner)

    print(d[0])


if __name__ == '__main__':
    main()
