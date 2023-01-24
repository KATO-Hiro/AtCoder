# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    if (2 * a == b) or (2 * a + 1 == b):
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
