# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    bit = 1 << x

    for _ in range(n):
        ai, bi = map(int, input().split())

        for _ in range(bi):
            bit |= bit >> ai

    if bit & 1:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
