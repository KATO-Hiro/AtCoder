# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    s = int(input())
    a = int(input())
    b = int(input())
    count = ceil(max(0, s - a) / b)
    
    print(250 + count * 100)


if __name__ == "__main__":
    main()
