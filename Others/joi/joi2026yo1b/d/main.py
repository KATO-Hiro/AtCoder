# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = list(map(int, input().split()))

    for i, ci in enumerate(c):
        summed = 0

        for j, cj in enumerate(c):
            if ci != cj:
                continue

            summed += abs(i - j)

        print(summed)


if __name__ == "__main__":
    main()
