# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    if a > (b * c):
        a = b * c
    
    print(a / b)


if __name__ == "__main__":
    main()
