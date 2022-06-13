# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(str, input().split())

    for ai, bi in zip(a[::-1], b[::-1]):
        if (int(ai) + int(bi)) >= 10:
            print("Hard")
            exit()
    
    print("Easy")


if __name__ == "__main__":
    main()
