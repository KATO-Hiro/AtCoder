# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = float("inf")

    for case in [0, 1]:
        count = 0
        summed = 0

        for index, ai in enumerate(a):
            summed += ai

            if index % 2 == case:
                if summed >= 0:
                    count += 1 + summed
                    summed = -1
            else:
                if summed <= 0:
                    count += 1 - summed
                    summed = 1

        ans = min(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
