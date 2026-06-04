# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, b = map(int, input().split())

    for i in range(10**7 + 1):
        if i * b > w * 1000:
            print(i)
            break


if __name__ == "__main__":
    main()
