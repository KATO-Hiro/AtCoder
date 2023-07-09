# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list()

    for _ in range(m):
        ki, *si = map(int, input().split())
        s.append(set(si))

    p = list(map(int, input().split()))

    patterns = product([0, 1], repeat=n)
    ans = 0

    for pattern in patterns:
        on_ids = set()

        for i, pattern_i in enumerate(pattern, 1):
            if pattern_i == 1:
                on_ids.add(i)

        count = 0

        for i, si in enumerate(s):
            if len(si & on_ids) % 2 == p[i]:
                count += 1

        if count == m:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
