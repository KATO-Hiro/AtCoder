# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    s = s.replace("A", "BB")
    s = s.replace("BB", "A")
    print(s)


if __name__ == "__main__":
    main()
