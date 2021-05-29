# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    summed, total = 0, 0
    max_value = 0

    for index, ai in enumerate(a):
        summed += ai
        total += summed
        max_value = max(max_value, ai)
        ans = total + max_value * (index + 1)
        print(ans)


if __name__ == "__main__":
    main()
