# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    x, a, b = map(int, input().split())
    xa = abs(x - a)
    xb = abs(x - b)

    if xa < xb:
        print("A")
    else:
        print("B")


if __name__ == "__main__":
    main()
