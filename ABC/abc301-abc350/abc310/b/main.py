# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [tuple(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        pi, ci, *fi = a[i]
        fi = set(fi)

        for j in range(n):
            if i == j:
                continue

            ok = True
            pj, cj, *fj = a[j]
            fj = set(fj)

            cond1 = pi >= pj
            count1 = 0

            for fik in fi:
                if fik in fj:
                    count1 += 1

            cond2 = count1 == ci
            count2 = 0

            for fjk in fj:
                if fjk not in fi:
                    count2 += 1

            cond3 = (pi > pj) or (count2 > 0)

            if cond1 == cond2 == cond3 == True:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
