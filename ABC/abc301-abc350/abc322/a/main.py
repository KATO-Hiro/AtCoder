# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = "ABC"

    if t not in s:
        print(-1)
        exit()

    for i in range(n):
        if i + 3 > n:
            break

        u = s[i : i + 3]

        if u == t:
            print(i + 1)
            exit()


if __name__ == "__main__":
    main()
