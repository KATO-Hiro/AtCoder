# -*- coding: utf-8 -*-


def main():
    from statistics import median

    n = int(input())
    aa = [0 for _ in range(n)]
    bb = [0 for _ in range(n)]

    for i in range(n):
        a, b = map(int, input().split())
        aa[i] = a
        bb[i] = b

    med_aa = median(aa)
    med_bb = median(bb)
    ans = (med_bb - med_aa) * n

    for ai in aa:
        if ai <= med_aa:
            ans += (med_aa - ai) * 2

    for bi in bb:
        if bi >= med_bb:
            ans += (bi - med_bb) * 2

    print(ans)


if __name__ == '__main__':
    main()
