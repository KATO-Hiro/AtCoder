# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    for si, ti in zip(s, s[1:]):
        u = si + ti

        if u == "ab" or u == "ba":
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
