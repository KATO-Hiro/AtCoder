# -*- coding: utf-8 -*-


def main():
    from math import log10
    import sys

    input = sys.stdin.readline
    
    n = int(input())

    if n * log10(2) > 2 * log10(n):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
