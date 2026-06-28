# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, m = map(int, input().split())
    dab = []
    c = Counter()

    for _ in range(n):
        ai, di, bi = map(int, input().split())

        if di == 1:
            ai = bi

        dab.append((di, ai, bi))
        c[ai] += 1

    dab.sort(reverse=True)
    size = len(c.keys())
    ans = [size]

    for day in range(1, m + 1):
        if len(dab) == 0 or day != dab[-1][0]:
            ans.append(ans[-1])
            continue

        while True:
            if len(dab) == 0:
                break

            if day != dab[-1][0]:
                break

            _, ai, bi = dab.pop()
            c[ai] -= 1

            if c[ai] == 0:
                del c[ai]

            c[bi] += 1

        ans.append(len(c.keys()))

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
