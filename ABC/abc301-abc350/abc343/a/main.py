# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c = a + b

    for i in range(10):
        if i != c:
            print(i)
            exit()


if __name__ == "__main__":
    main()
