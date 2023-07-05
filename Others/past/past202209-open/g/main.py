# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import product

    input = sys.stdin.readline

    n, l, k = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    ans = 0

    for pattern in product([0, 1], repeat=l):
        if sum(pattern) != k:
            continue

        d = defaultdict(int)

        for si in s:
            t = list()

            for pi, sij in zip(pattern, si):
                if pi == 0:
                    t += [sij]
                else:
                    t += ["A"]

            d["".join(t)] += 1

        ans = max(ans, max(d.values()))

    print(ans)


if __name__ == "__main__":
    main()
