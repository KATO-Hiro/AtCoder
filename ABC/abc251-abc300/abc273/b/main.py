# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    for i in range(1, k + 1):
        q = n % (10 ** i)

        if q >= 5 * (10 ** (i - 1)):
            n += (10 ** i)

        n -= q
    
    print(n)


if __name__ == "__main__":
    main()
