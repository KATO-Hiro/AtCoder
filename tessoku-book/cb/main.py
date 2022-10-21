# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for x, y, z in combinations(a, 3):
        if (x + y + z) == 1000:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
