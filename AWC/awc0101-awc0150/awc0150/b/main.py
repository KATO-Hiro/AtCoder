# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 1

    for _ in range(n):
        ai = int(input())
        ans *= ai

    print(ans)


if __name__ == "__main__":
    main()
