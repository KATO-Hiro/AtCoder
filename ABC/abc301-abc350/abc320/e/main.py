# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    n, m = map(int, input().split())
    out = []
    waiting = [i for i in range(n)]
    ans = [0] * n

    for _ in range(m):
        ti, wi, si = map(int, input().split())

        while len(out) > 0:
            ui, id = heappop(out)

            if ui <= ti:
                heappush(waiting, id)
            else:
                heappush(out, (ui, id))
                break

        if len(waiting) > 0:
            id = heappop(waiting)
            ans[id] += wi
            heappush(out, (ti + si, id))

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
