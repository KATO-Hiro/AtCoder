# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    d, n = map(int, input().split())

    if n == 100:
        n += 1
    
    print(100 ** d * n)


if __name__ == "__main__":
    main()
