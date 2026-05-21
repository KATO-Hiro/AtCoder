# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    n = int(input())

    for _ in range(2):
        for _ in range(n):
            s.pop()

        s = s[::-1]

    print("".join(s))


if __name__ == "__main__":
    main()
