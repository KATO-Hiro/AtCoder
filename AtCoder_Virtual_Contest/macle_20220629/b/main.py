# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    two_count = 0
    four_count = 0

    for ai in a:
        if ai % 4 == 0:
            four_count += 1
        elif ai % 2 == 0:
            two_count += 1
    
    m = n - two_count

    if two_count == 0:
        if m // 2 <= four_count:
            print("Yes")
        else:
            print("No")
    elif ceil(m / 2) <= four_count:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
