# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    inf = 10**18
    summed = 0
    value_min = 0
    ans = -inf

    for ai in a:
        summed += ai
        ans = max(ans, summed - value_min)
        value_min = min(value_min, summed)

    print(ans)


if __name__ == "__main__":
    main()
