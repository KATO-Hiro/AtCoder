# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    s = input().rstrip()

    for i in range(1, n):
        first, second = "".join(s[:i]), "".join(s[i:])

        if first < second:
            print("Yes")
            return

    print("No")
    return


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
