# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        else:
            print(i)


if __name__ == "__main__":
    main()
