# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)
    s = list()

    for _ in range(n):
        si = input().rstrip()
        s.append(si)
        m = len(si)
        used = set()

        for pattern in product([0, 1], repeat=m):
            t = ""

            for pi, sij in zip(pattern, si):
                if pi == 0:
                    continue

                t += sij

            if t not in used:
                d[t] += 1
                used.add(t)

    ans = 0

    for si in s:
        ans += d[si]

    print(ans)


if __name__ == "__main__":
    main()
