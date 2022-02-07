# -*- coding: utf-8 -*-


def main():
    from math import log10
    import sys

    input = sys.stdin.readline
    
    n = int(input())

    if n < 2 or n > 4:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
