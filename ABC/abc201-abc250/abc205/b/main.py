# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))

    for index, ai in enumerate(a, 1):
        if index != ai:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
