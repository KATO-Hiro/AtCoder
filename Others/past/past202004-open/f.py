# -*- coding: utf-8 -*-


def main():
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline

    n = int(input())
    points = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        points.append((ai - 1, bi))

    p = sorted(points)
    elements = list()

    index = 0
    total = 0

    for i in range(n):
        while index < n and p[index][0] == i:
            heappush(elements, -p[index][1])

            index += 1

        total += -heappop(elements)
        print(total)


if __name__ == '__main__':
    main()
