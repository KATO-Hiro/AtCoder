# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = ""

    for si in s:
        if si == "A":
            ans += si
        else:
            ans += "."

    print(ans)


if __name__ == "__main__":
    main()
