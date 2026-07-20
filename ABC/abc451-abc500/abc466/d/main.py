# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    r = [set() for _ in range(n)]
    c = [set() for _ in range(n)]

    for _ in range(m):
        ri, ci = map(int, input().split())
        ri -= 1
        ci -= 1

        for cj in r[ri]:
            c[cj].discard(ri)

        for rj in c[ci]:
            r[rj].discard(ci)

        r[ri] = set([ci])
        c[ci] = set([ri])

    ans = sum([len(ri) for ri in r])
    print(ans)


if __name__ == "__main__":
    main()
