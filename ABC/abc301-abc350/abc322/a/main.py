# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = "ABC"

    index = s.find(t)

    if index != -1:
        index += 1

    print(index)


if __name__ == "__main__":
    main()
