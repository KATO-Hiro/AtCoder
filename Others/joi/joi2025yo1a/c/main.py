# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = ""

    for si in s:
        if si == "J":
            ans += "O"
        elif si == "O":
            ans += "I"
        elif si == "I":
            ans += "J"

    print(ans)


if __name__ == "__main__":
    main()
