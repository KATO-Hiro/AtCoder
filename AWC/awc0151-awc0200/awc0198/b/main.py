# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())[::-1]
    ans = -1

    for i, si in enumerate(s):
        if si != "D":
            continue

        ans = n - i
        break

    print(ans)


if __name__ == "__main__":
    main()
