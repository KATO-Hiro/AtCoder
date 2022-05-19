# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list()

    for i in range(m):
        si = list(map(int, input().split()))[1:]
        s.append(si)

    p = list(map(int, input().split()))

    patterns = product([0, 1], repeat=n)
    ans = 0

    for pattern in patterns:
        on = [i for i, pi in enumerate(pattern, 1) if pi == 1]
        switch_count = 0

        for j, si in enumerate(s):
            common = len(set(on) & set(si))
            
            if common % 2 == p[j]:
                switch_count += 1

        if switch_count == m:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
