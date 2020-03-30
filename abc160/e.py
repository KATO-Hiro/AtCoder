# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    from heapq import heappush, heappop

    x, y, a, b, c = map(int, input().split())
    p = sorted(list(map(int, input().split())), reverse=True)[:x]
    q = sorted(list(map(int, input().split())), reverse=True)[:y]
    r = sorted(list(map(int, input().split())), reverse=True)

    h = list()

    for pi in p:
        heappush(h, pi)

    for qi in q:
        heappush(h, qi)

    for ri in r:
        heappush(h, ri)

    for i in range(c):
        heappop(h)

    print(sum(h))


if __name__ == '__main__':
    main()
