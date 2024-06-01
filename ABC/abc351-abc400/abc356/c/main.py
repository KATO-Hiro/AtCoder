# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

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

    for pattern in product([0, 1], repeat=n):
        matched = 0

        for i in range(m):
            count = 0

            for aij in a[i]:
                count += pattern[aij - 1]

            if (count >= k and is_open[i]) or (count < k and not is_open[i]):
                matched += 1

        if matched == m:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
