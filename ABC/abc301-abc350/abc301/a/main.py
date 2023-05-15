# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = s.count("T")
    a = n - t

    if t > a:
        print("T")
    elif t < a:
        print("A")
    else:
        if s[-1] == "T":
            print("A")
        else:
            print("T")


if __name__ == "__main__":
    main()
