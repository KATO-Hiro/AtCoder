# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    v, a, b, c = map(int, input().split())
    v %= (a + b + c)

    if v - a < 0:
        print("F")
    elif v - (a + b) < 0:
        print("M")
    else:
        print("T")



if __name__ == "__main__":
    main()
