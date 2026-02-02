# -*- coding: utf-8 -*-


def main():
    import sys
    from functools import cmp_to_key

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]

    def compare(a, b):
        ai, aj = a
        bi, bj = b
        diff = ai * bj - aj * bi

        if diff > 0:
            return 1
        elif diff < 0:
            return -1
        else:
            return 0

    ans = sorted(ab, key=cmp_to_key(compare))

    for ai, bi in ans:
        print(ai, bi)


if __name__ == "__main__":
    main()
