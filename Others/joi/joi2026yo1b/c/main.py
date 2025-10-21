# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = 0

    for i in range(n):
        if i + 2 >= n:
            break

        if s[i : i + 3] == "AOI" or s[i : i + 3] == "IOI":
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
