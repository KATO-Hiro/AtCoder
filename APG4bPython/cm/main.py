# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_mean = sum(a) // n

    for ai in a:
        print(abs(ai - a_mean))


if __name__ == "__main__":
    main()
