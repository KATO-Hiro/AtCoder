# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    abc = [tuple(map(int, input().split())) for _ in range(n - 1)]
    imos = [0] * (n + 1)

    for p1, p2 in zip(p, p[1:]):
        if p1 > p2:
            p1, p2 = p2, p1

        imos[p1 - 1] += 1
        imos[p2 - 1] -= 1
        # print(p1, p2)

    imos = list(accumulate(imos))
    # print(imos)
    ans = 0

    for i, (ai, bi, ci) in enumerate(abc):
        count = imos[i]
        ans += min(ai * count, bi * count + ci)

    print(ans)


if __name__ == "__main__":
    main()
