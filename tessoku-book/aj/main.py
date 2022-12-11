# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    diff = k - 2 * (n - 1)

    if diff < 0 or diff % 2 == 1:
        print("No")
    else:
        print("Yes")
    

if __name__ == "__main__":
    main()
