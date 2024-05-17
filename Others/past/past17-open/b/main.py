# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    if s.count("Perfect") == n:
        print("All Perfect")
    elif s.count("Great") + s.count("Perfect") == n:
        print("Full Combo")
    else:
        print("Failed")


if __name__ == "__main__":
    main()
