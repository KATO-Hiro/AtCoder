# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    max_a, min_a = max(a), min(a)

    print(sum(a) - max_a - min_a)


if __name__ == "__main__":
    main()
