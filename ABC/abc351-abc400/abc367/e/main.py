# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    x = list(map(lambda xi: int(xi) - 1, input().split()))
    a = list(map(int, input().split()))

    def prod(x, y):
        return [y[xi] for xi in x]

    b = list(range(n))

    while k > 0:
        if k & 1:
            b = prod(b, x)

        k >>= 1
        x = prod(x, x)  # Doubling

    print(*prod(b, a))


if __name__ == "__main__":
    main()
