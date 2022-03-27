# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for i in range(2000 + 1):
        if i not in a:
            print(i)
            exit()


if __name__ == "__main__":
    main()
