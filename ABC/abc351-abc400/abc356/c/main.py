# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list()
    is_open = [False] * m

    for i in range(m):
        _, *ar = input().rstrip().split()
        *ai, ri = ar
        ai = list(map(int, ai))
        a.append(list(map(int, ai)))

        if ri == "o":
            is_open[i] = True

    ans = 0

    for bit in range(1 << n):
        ok = True

        for i in range(m):
            count = 0

            for aij in a[i]:
                if bit & (1 << (aij - 1)):
                    count += 1

            if (count >= k) != is_open[i]:
                ok = False

        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
