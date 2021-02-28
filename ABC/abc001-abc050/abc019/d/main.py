# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    index = 0
    dist = 0

    for i in range(2, n + 1):
        print("?", 1, i, flush=True)

        di = int(input())

        if di > dist:
            dist = di
            index = i

    index2 = 0
    dist2 = 0

    for j in range(1, n + 1):
        if j == index:
            continue

        print("?", index, j, flush=True)

        di = int(input())

        if di > dist2:
            dist2 = di
            index2 = j

    dist_max = max(dist, dist2)
    print("!", dist_max)


if __name__ == "__main__":
    main()
