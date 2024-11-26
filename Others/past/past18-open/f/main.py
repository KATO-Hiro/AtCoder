# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = int(input())

    for _ in range(n):
        ci, vi = input().rstrip().split()
        s = s.replace(ci, vi)

    print(eval(s))


if __name__ == "__main__":
    main()
