# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, a = map(int, input().split())
    numbers = [0] + [i for i in range(1, n + 1)] * 1000
    print(numbers[a + k - 1])


if __name__ == "__main__":
    main()
