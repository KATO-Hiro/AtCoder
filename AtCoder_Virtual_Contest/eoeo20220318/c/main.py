# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    alpha = min(a, min(b, min(c, min(d, e))))
    
    print(ceil(n / alpha) + 5 - 1)


if __name__ == "__main__":
    main()
