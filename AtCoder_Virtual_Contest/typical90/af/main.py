# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    xy = set(list(tuple(map(int, input().split())) for _ in range(m)))
    inf = 10**12
    ans = inf

    for pattern in permutations(range(1, n + 1), n):
        ok = True

        for pi, pj in zip(pattern, pattern[1:]):
            if (pi, pj) in xy or (pj, pi) in xy:
                ok = False
                break

        if ok:
            cost = 0

            for i, pi in enumerate(pattern):
                cost += a[pi - 1][i]

            ans = min(ans, cost)

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
