# -*- coding: utf-8 -*-


def compare(a, b):
    ai, aj, i = a
    bi, bj, j = b
    diff = ai * bj - bi * aj

    if diff > 0:
        return 1
    elif diff < 0:
        return -1
    else:
        return 0


def main():
    import sys
    from functools import cmp_to_key

    input = sys.stdin.readline

    n = int(input())
    ab = list()

    for i in range(1, n + 1):
        ai, bi = map(int, input().split())
        ab.append((ai, bi, i))

    ans = sorted(
        ab,
        key=cmp_to_key(compare),
        reverse=True,
    )

    print(*[i for _, _, i in ans])


if __name__ == "__main__":
    main()
