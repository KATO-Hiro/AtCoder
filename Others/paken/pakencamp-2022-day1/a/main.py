# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    if x == 0 and y == 0:
        print(0)
    elif x == 0 or y == 0:
        print(1)
    else:
        print(2)
    

if __name__ == "__main__":
    main()
