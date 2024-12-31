# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    h, w, z = map(int, input().split())
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    s = [list(map(int, input().split())) for _ in range(h)]

    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    heap = []
    ans = s[p][q]
    added = [[False] * w for _ in range(h)]
    added[p][q] = True

    def f(cur_y, cur_x):
        for dx, dy in dxy:
            ny = cur_y + dy
            nx = cur_x + dx

            if not (0 <= ny < h):
                continue
            if not (0 <= nx < w):
                continue

            if added[ny][nx]:
                continue

            heappush(heap, (s[ny][nx], ny, nx))
            added[ny][nx] = True

    f(p, q)

    while heap:
        score, cur_y, cur_x = heap[0]

        if score * z >= ans:
            break

        ans += score
        heappop(heap)
        f(cur_y, cur_x)

    print(ans)


if __name__ == "__main__":
    main()
