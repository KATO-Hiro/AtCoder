# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n, m = map(int, input().split())
    pending = -1
    dist = [[pending for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        dist[ai][bi] = ci
        dist[bi][ai] = ci

    # print(dist)
    ans = 0

    # 頂点の順列を全列挙
    for pattern in permutations(range(n)):
        candidate = 0

        for frm, to in zip(pattern, pattern[1:]):
            if dist[frm][to] == pending:
                break

            candidate += dist[frm][to]

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
