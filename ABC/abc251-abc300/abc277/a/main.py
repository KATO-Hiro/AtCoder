# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    p = list(map(int, input().split()))

    for index, pi in enumerate(p, 1):
        if pi == x:
            print(index)
            exit()
    

if __name__ == "__main__":
    main()
