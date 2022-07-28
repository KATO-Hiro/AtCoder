# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sum(a) // n
    ans = [0] * n

    for i, ai in enumerate(a):
        ans[i] = abs(ai - b)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
