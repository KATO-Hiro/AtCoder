# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import combinations

    input = sys.stdin.readline

    h, w, d = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    e = defaultdict(set)

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue

            pos = set()
            pos.add((i, j))

            for k in range(h):
                for l in range(w):
                    if s[k][l] == "#":
                        continue

                    if k == i and l == j:
                        continue

                    if abs(i - k) + abs(j - l) <= d:
                        pos.add((k, l))

            e[(i, j)] = pos

    ans = 0

    for e1, e2 in combinations(e.values(), 2):
        ans = max(ans, len(e1 | e2))

    print(ans)


if __name__ == "__main__":
    main()
