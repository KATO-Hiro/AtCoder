# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for i in range(t):
        li, ri = map(int, input().split())

        max_value = ri - li
        min_value = ri - max_value
        count = max_value - min_value + 1

        if max_value < li or min_value < li:
            print(0)
        else:
            print(count * (count + 1) // 2)


if __name__ == "__main__":
    main()
