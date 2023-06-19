# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = set()

    for i in range(1, n + 1):
        si = input().rstrip()

        if si not in s:
            print(i)
            s.add(si)


if __name__ == "__main__":
    main()
