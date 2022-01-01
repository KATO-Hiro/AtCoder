# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    cd = [tuple(map(int, input().split())) for _ in range(m)]

    for p in permutations(range(1, n + 1)):
        ok = True

        for ai, bi in ab:
            pi = p[ai - 1]
            pj = p[bi - 1]

            if (pi, pj) not in cd and (pj, pi) not in cd:
                ok = False
                break

        if ok:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
