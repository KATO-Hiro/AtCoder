# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = set()

    for _ in range(n):
        si = input().rstrip()
        t.add(min(si, si[::-1]))

    print(len(t))


if __name__ == "__main__":
    main()
