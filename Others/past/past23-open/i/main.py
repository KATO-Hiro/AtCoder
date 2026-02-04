# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, y = map(int, input().split())
    sx = []

    for _ in range(n):
        si, xi = map(str, input().split())
        sx.append((si, int(xi)))

    ans = 0

    for pattern in product([0, 1], repeat=n):
        cost = 0
        t = set()
        ok = True

        for i, pi in enumerate(pattern):
            if pi == 0:
                continue

            si, xi = sx[i]
            cost += xi

            if cost > y:
                ok = False
                break

            for sij in si:
                t.add(sij)

        if cost > y:
            ok = False
        if ok:
            ans = max(ans, len(t))

    print(ans)


if __name__ == "__main__":
    main()
