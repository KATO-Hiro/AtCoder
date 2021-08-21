# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0

    for index, ai in enumerate(a, 1):
        if index % 2 == 0:
            total += ai - 1
        else:
            total += ai
    
    if total <= x:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
