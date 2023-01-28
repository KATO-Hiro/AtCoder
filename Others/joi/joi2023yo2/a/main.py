# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_min, a_max = min(a), max(a)

    for ai in a:
        print(max(abs(ai - a_min), abs(a_max - ai)))
    

if __name__ == "__main__":
    main()
