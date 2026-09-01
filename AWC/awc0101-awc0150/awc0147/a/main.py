# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)

    for i, ai in enumerate(a, 1):
        if ai == a_max:
            print(i)
            exit()


if __name__ == "__main__":
    main()
