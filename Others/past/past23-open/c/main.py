# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()

    for i, si in enumerate(s, 1):
        if i <= k:
            continue

        if si == "o":
            print(i)
            exit()


if __name__ == "__main__":
    main()
