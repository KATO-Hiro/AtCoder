# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    uv = []

    for _ in range(m):
        ui, vi = map(int, input().split())
        uv.append((ui - 1, vi - 1))

    ans = 0

    for pattern in permutations(range(n)):
        ok = True

        pos = defaultdict(int)
        candidate = 0

        for i, pi in enumerate(pattern):
            pos[pi] = i
            candidate += a[pi] * (i + 1)

        for ui, vi in uv:
            if pos[ui] > pos[vi]:
                ok = False
                break

        if not ok:
            continue

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
