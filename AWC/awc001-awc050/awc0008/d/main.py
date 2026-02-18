# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappush, heappop

    input = sys.stdin.readline

    n, m = map(int, input().split())
    hq = []

    for _ in range(n):
        fi, di = map(int, input().split())
        heappush(hq, (-fi, -fi, di, 1))

    ans = 0

    def f(fj, dj, j):
        return max(fj - (j - 1) * dj, 0)

    for _ in range(m):
        _, fj, dj, j = heappop(hq)
        fj *= -1

        fk = f(fj, dj, j)
        ans += fk
        nfj = f(fj, dj, j + 1)

        heappush(hq, (-nfj, -fj, dj, j + 1))

    print(ans)


if __name__ == "__main__":
    main()
