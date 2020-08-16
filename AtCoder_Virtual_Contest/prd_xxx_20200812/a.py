# -*- coding: utf-8 -*-


def main():
    from heapq import heappush, heappop

    n = int(input())
    a = list(map(int, input().split()))
    elements = list()

    for ai in a:
        heappush(elements, ai)

    while len(elements) >= 2:
        a_min = heappop(elements)

        for _ in range(len(elements)):
            aj = heappop(elements)
            aj %= a_min

            if aj != 0:
                heappush(elements, aj)

        if len(elements) == 0:
            print(a_min)
            exit()

    print(min(a_min, min(elements)))


if __name__ == '__main__':
    main()
