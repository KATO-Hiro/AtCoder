# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, c1, c2 = input().rstrip().split()
    s = input().rstrip()
    ans = ""

    for si in s:
        if si == c1:
            ans += c1
        else:
            ans += c2

    print(ans)


if __name__ == "__main__":
    main()
