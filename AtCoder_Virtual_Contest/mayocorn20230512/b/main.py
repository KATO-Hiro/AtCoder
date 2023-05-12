# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    st = [tuple(map(str, input().rstrip().split())) for _ in range(n)]
    d = defaultdict(int)
    candidates = list()

    for i, (si, ti) in enumerate(st, 1):
        ti = int(ti)

        if si not in d.keys():
            candidates.append((ti, i))
            d[si] += 1

    candidates = sorted(candidates, key=lambda x: (x[0], -x[1]), reverse=True)

    print(candidates[0][1])


if __name__ == "__main__":
    main()
