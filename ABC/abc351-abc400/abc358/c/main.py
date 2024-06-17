# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    ans = n

    for pattern in product([0, 1], repeat=n):
        t = set()

        for i, p in enumerate(pattern):
            if p == 0:
                continue

            for j, sij in enumerate(s[i]):
                if sij == "o":
                    t.add(j)

        if len(t) == m:
            ans = min(ans, sum(pattern))

    print(ans)


if __name__ == "__main__":
    main()
