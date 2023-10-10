# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    pcf = [tuple(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        pi, ci, *fi = pcf[i]

        for j in range(n):
            if i == j:
                continue

            flag = True
            pj, cj, *fj = pcf[j]

            if not (pi >= pj):
                flag = False

            if not (set(fj) >= set(fi)):
                flag = False

            if not (pi > pj or set(fj) > set(fi)):
                flag = False

            if flag:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
