# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, op, b = input().rstrip().split()
    a, b = int(a), int(b)

    if op == "+":
        print(a + b)
    else:
        print(a - b)


if __name__ == "__main__":
    main()
