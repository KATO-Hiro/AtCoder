# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    d = defaultdict(int)
    ans = n * (n - 1) // 2  # nC2

    for ai in a:
        for aj, ak in zip(ai, ai[1:]):
            if (aj, ak) not in d.keys() and (ak, aj) not in d.keys():
                d[(aj, ak)] += 1

    ans -= len(d.keys())

    print(ans)


if __name__ == "__main__":
    main()
