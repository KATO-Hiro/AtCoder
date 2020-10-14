# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline
    numbers = list(map(int, input().split()))
    total = sum(numbers)

    for i in range(1, 4):
        for j in combinations(range(4), i):
            tmp = 0

            for k in j:
                tmp += numbers[k]

            if tmp * 2 == total:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
