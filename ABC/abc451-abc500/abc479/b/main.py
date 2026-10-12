# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans, count = 0, 0

    for si in s:
        if si == "R":
            count += 1
            ans = max(ans, count)
        else:
            count = 0

    print(ans)


if __name__ == "__main__":
    main()
