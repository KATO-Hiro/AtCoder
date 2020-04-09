# -*- coding: utf-8 -*-


def main():
    from math import pi
    import sys
    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list()
    r = list()
    h = list()

    for i in range(n):
        xi, ri, hi = map(int, input().split())
        x.append(xi)
        r.append(ri)
        h.append(hi)

    ans = [0 for _ in range(q)]

    for j in range(q):
        ai, bi = map(int, input().split())
        total = 0

        for xi, ri, hi in zip(x, r, h):
            if (bi < xi) or (ai > (xi + hi)):
                continue

            yi = xi + hi
            vi = (ri ** 2) * hi

            if ai <= xi:
                if bi >= yi:
                    total += vi
                else:
                    vs = vi * (((yi - bi) ** 3) / (hi ** 3))
                    total += vi - vs
            elif ai > xi:
                if bi >= yi:
                    vs = vi * (((yi - ai) ** 3) / (hi ** 3))
                    total += vs
                else:
                    vya = vi * (((yi - ai) ** 3) / (hi ** 3))
                    vyb = vya * (((yi - bi) ** 3) / ((yi - ai) ** 3))
                    total += vya - vyb

        ans[j] = total * pi / 3

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
