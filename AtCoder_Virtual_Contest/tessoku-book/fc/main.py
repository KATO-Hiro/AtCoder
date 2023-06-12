# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    patterns = sorted(list(product(["4", "7"], repeat=10)))
    print("".join(patterns[n - 1]))


if __name__ == "__main__":
    main()
