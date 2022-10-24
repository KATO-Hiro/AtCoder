# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    a, b = map(int, input().split())
    c = b / a
    d = 4
    d -= 1
    print(f'{c:.{d}f}')


if __name__ == "__main__":
    main()
