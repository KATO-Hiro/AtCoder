# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    a, n = map(int, input().split())
    digit = len(list(str(n)))
    upper = (10**digit) - 1
    d = deque()
    d.append(1)
    inf = 10**18
    size = 10**6 + 1
    dist = [inf] * size
    dist[1] = 0
    visited = [False] * size
    ans = -1

    while d:
        di: int = d.popleft()

        if di == n:
            ans = dist[n]
            break
        if di > upper:
            break
        if visited[di]:
            continue

        visited[di] = True

        if di >= 10 and di % 10 != 0:
            tmp = str(di)
            ndi = int(tmp[-1] + tmp[:-1])

            if ndi <= upper:
                dist[ndi] = min(dist[ndi], dist[di] + 1)
                d.append(ndi)

        if di * a <= upper:
            dist[di * a] = min(dist[di * a], dist[di] + 1)
            d.append(di * a)

    print(ans)


if __name__ == "__main__":
    main()
