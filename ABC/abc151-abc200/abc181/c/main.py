# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = list()

    for i in range(n):
        xi, yi = map(int, input().split())
        xy.append((xi, yi))

    for first, second, third in list(permutations(xy, 3)):
        if first == second or second == third or third == first:
            continue

        x1, y1 = first[0], first[1]
        x2, y2 = second[0], second[1]
        x3, y3 = third[0], third[1]

        result = (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)

        if result:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
