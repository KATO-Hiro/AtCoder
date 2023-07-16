# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    pcf = [tuple(map(int, input().split())) for _ in range(n)]

    for i, (pi, ci, *fi) in enumerate(pcf):
        for j, (pj, cj, *fj) in enumerate(pcf):
            if i == j:
                continue

            ok = True
            fi, fj = set(fi), set(fj)

            if not (pi >= pj):
                ok = False
            if not fj.issuperset(fi):
                ok = False
            if not ((pi > pj) or (len(fj) > len(fi))):
                ok = False

            if ok:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
