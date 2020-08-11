# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    d = dict()
    ans = [[0] for _ in range(n + 1)]

    for i in range(m):
        ai, bi = map(int, input().split())

        if ai not in d.keys():
            d[ai] = list()
        if bi not in d.keys():
            d[bi] = list()

        d[bi].append(ai)
        d[ai].append(bi)

    for x in d.keys():
        for y in d[x]:
            for z in d[y]:
                if z != x and z not in d[x] and z not in ans[x]:
                    ans[x].append(z)

    for k in range(1, n + 1):
        print(len(ans[k]) - 1)


if __name__ == '__main__':
    main()
