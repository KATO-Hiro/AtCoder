# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    a = list()
    a_max = 0

    for _ in range(n):
        _, *ai = map(int, input().split())
        a_max = max(a_max, max(ai))
        a.append(set(ai))

    ans = 0

    for pattern in product([0, 1], repeat=n):
        s = set(range(1, a_max + 1))
        ok = True

        if sum(pattern) <= 1:
            continue

        for i, pi in enumerate(pattern):
            if pi == 0:
                continue

            s &= a[i]

        for si in s:
            if si % 2 == 0:
                ok = False
                break

        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
