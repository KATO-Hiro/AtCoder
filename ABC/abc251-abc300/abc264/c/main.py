# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    rows = list(product([0, 1], repeat=h1))
    cols = list(product([0, 1], repeat=w1))

    for row in rows:
        if sum(row) != h2:
            continue

        for col in cols:
            if sum(col) != w2:
                continue

            c = list()

            for i, ri in enumerate(row):
                if ri == 0:
                    continue

                tmp = list()

                for j, cj in enumerate(col):
                    if cj == 0:
                        continue

                    tmp.append(a[i][j])
                
                c.append(tmp)
            
            count = 0

            for i in range(h2):
                for j in range(w2):
                    if c[i][j] == b[i][j]:
                        count += 1
            
            if count == h2 * w2:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
