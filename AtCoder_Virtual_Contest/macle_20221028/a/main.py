# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = [i for i in range(1, n + 1)]

    if a == b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
