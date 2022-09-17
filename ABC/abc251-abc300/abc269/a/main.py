# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    
    print((a + b) * (c - d))
    print("Takahashi")


if __name__ == "__main__":
    main()
