# -*- coding: utf-8 -*-


def main():
    from math import floor
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    value_max = 10000

    for i in range(1, value_max):
        if floor(i * 0.08) == a and floor(i * 0.1) == b:
            print(i)
            exit()
    
    print(-1)


if __name__ == "__main__":
    main()
