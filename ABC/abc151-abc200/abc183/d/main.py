# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    from itertools import accumulate

    n, w = map(int, input().split())
    volumes = [0 for _ in range(2 * (10 ** 5) + 10)]

    for i in range(n):
        si, ti, pi = map(int, input().split())

        volumes[si] += pi
        volumes[ti] -= pi

    v = list(accumulate(volumes))
    v_max = max(v)

    if v_max > w:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
