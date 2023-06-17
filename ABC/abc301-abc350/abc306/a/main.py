# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = ""

    for si in s:
        ans += si * 2

    print(ans)


if __name__ == "__main__":
    main()
