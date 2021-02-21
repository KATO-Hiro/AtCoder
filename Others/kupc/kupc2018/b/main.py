# -*- coding: utf-8 -*-


def solve(ai, bi, ci):
    summed = (100 * ai) + (10 * bi) + ci

    if summed % 2 == 1:
        return "No"

    summed //= 2

    summed -= 100 * min(summed // 100, ai)
    summed -= 10 * min(summed // 10, bi)
    summed -= min(summed, ci)

    if summed == 0:
        return "Yes"
    else:
        return "No"


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for i in range(n):
        ai, bi, ci = map(int, input().split())

        print(solve(ai, bi, ci))


if __name__ == "__main__":
    main()
