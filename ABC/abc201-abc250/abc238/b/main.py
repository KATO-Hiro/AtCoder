# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    summed = 0
    rad = set()
    rad.add(0)
    rad.add(360)

    for ai in a:
        summed += ai
        rad.add(summed % 360)
    
    sorted_rad = sorted(rad)
    ans = 0

    for first, second in zip(sorted_rad, sorted_rad[1:]):
        ans = max(ans, second - first)

    print(ans)


if __name__ == "__main__":
    main()
