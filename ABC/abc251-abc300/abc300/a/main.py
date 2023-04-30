# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = a + b

    for i, ci in enumerate(c, 1):
        if ci == d:
            print(i)
            exit()
    

if __name__ == "__main__":
    main()
