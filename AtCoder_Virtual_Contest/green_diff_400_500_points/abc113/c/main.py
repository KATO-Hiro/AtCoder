# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(list)

    for i in range(m):
        pi, yi = map(int, input().split())
        d[pi].append((yi, i))

    ans = [""] * m

    for pi in d.keys():
        for j, (_, i) in enumerate(sorted(d[pi]), 1):
            ans[i] = str(pi).zfill(6) + str(j).zfill(6)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
