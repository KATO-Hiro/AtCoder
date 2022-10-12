# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in range(m)]
    e = list(map(int, input().split()))
    inf = 10 ** 18
    dist = [inf] * n
    dist[0] = 0
    start = False

    for ei in e:
        ei -= 1

        ai, bi, ci = abc[ei]
        ai -= 1
        bi -= 1

        if ai == 0:
            start = True
        
        # 都市1からスタートしていない
        if not start:
            continue 

        # 都市aiに到達できていない
        if dist[ai] == inf:
            continue

        dist[bi] = min(dist[bi], dist[ai] + ci)

    ans = dist[n - 1]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
