# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappush, heappop

    input = sys.stdin.readline

    n = int(input())
    hq = list()

    for _ in range(n):
        li, ri = map(int, input().split())
        heappush(hq, (li, ri))

    ans = 0
    li, ri = -1, -1

    while hq:
        lj, rj = heappop(hq)

        if lj > ri:
            li, ri = lj, rj
            ans += 1
        else:
            ri = min(ri, rj)

    print(ans)


if __name__ == "__main__":
    main()
