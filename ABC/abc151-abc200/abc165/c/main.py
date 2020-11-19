# -*- coding: utf-8 -*-


def main():
    from itertools import combinations_with_replacement
    import sys

    input = sys.stdin.readline

    n, m, q = map(int, input().split())
    abcds = [list(map(int, input().split())) for _ in range(q)]

    numbers = list(combinations_with_replacement(range(1, m + 1), r=n))
    ans = 0

    for number in numbers:
        total = 0

        for abcd in abcds:
            ai, bi, ci, di = abcd[0], abcd[1], abcd[2], abcd[3]

            if number[bi - 1] - number[ai - 1] == ci:
                total += di

        ans = max(ans, total)

    print(ans)


if __name__ == "__main__":
    main()
