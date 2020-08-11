# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    bools = [[0 for __ in range(n)] for _ in range(m)]

    for i in range(m):
        si = list(map(int, input().split()))[1:]

        for sii in si:
            bools[i][sii - 1] = 1

    p = list(map(int, input().split()))
    ans = 0

    for bit in range(1 << n):
        count = 0

        for mi in range(m):
            # pattern = list()
            total = 0

            for ni in range(n):
                if bit & (1 << ni):
                    total += bools[mi][ni]

            if total % 2 == p[mi]:
                count += 1

        if count == m:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
