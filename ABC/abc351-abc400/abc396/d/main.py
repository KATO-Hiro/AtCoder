# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import pairwise, permutations

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10**20
    weights = defaultdict(int)

    for _ in range(m):
        ai, bi, wi = map(int, input().split())
        ai -= 1
        bi -= 1

        weights[(ai, bi)] = wi
        weights[(bi, ai)] = wi

    ans = inf

    for size in range(n - 1):
        for pattern in permutations(range(1, n - 1), size):
            path = [0] + list(pattern) + [n - 1]

            candidate = 0
            ok = True

            for first, second in pairwise(path):
                if (first, second) not in weights:
                    ok = False
                    break

                candidate ^= weights[(first, second)]

            if ok:
                ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
