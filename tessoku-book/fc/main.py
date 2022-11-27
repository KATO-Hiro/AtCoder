# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    numbers = list()
    n = int(input())

    for pattern in product(["4", "7"], repeat=10):
        numbers.append(int("".join(pattern)))
    
    print(sorted(numbers)[n - 1])


if __name__ == "__main__":
    main()
