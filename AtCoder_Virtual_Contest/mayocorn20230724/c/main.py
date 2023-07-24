# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    for h_pattern in product([0, 1], repeat=h1):
        if sum(h_pattern) != h2:
            continue

        c = list()

        for i, hi in enumerate(h_pattern):
            if hi == 1:
                c.append(a[i])

        for w_pattern in product([0, 1], repeat=w1):
            if sum(w_pattern) != w2:
                continue

            d = [[] for _ in range(h2)]

            for j, wj in enumerate(w_pattern):
                if wj == 0:
                    continue

                for i in range(h2):
                    d[i].append(c[i][j])

            if len(d) == 0:
                continue

            # print(d)

            if b == d:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
