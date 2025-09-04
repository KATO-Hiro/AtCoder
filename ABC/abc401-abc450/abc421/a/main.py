# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    x, y = map(str, input().split())
    x = int(x) - 1

    if s[x] == y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
