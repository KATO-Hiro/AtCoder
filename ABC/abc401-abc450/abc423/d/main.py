# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    n, k = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in range(n)]
    count, now = 0, 0
    ans = [0] * n
    hq = []

    for i, (ai, bi, ci) in enumerate(abc):
        now = max(now, ai)

        while ci + count > k and hq:
            bj, cj = heappop(hq)
            now = max(now, bj)
            count -= cj

        ans[i] = now
        heappush(hq, (now + bi, ci))
        count += ci

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
