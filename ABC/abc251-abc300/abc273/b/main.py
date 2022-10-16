# -*- coding: utf-8 -*-


def round_int(n: int, base: int, digit: int):
    """
    See:
    https://atcoder.jp/contests/abc273/submissions/35663188
    """

    assert base > 0

    for _ in range(digit):
        n, q = divmod(n, base)

        if q >= 5:
            n += 1
    
    return n * (base ** digit)


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    print(round_int(n, 10, k))


if __name__ == "__main__":
    main()
