# -*- coding: utf-8 -*-


def main():
    from heapq import heappush, heappop

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list()

    for ai in a:
        heappush(b, -ai)

    for i in range(m):
        bi = -heappop(b)
        bi //= 2
        heappush(b, -bi)

    print(-sum(b))


if __name__ == '__main__':
    main()
