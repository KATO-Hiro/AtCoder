# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    if 2 * s.count("For") >= n:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
