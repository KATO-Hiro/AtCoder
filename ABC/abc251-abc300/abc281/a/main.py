# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for i in range(n, -1, -1):
        print(i)
    

if __name__ == "__main__":
    main()
