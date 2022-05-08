# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = Counter(list(map(int, input().split())))
    b = Counter(list(map(int, input().split())))
    
    if (b - a):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
