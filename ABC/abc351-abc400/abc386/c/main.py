# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    s = list(input().rstrip())
    t = list(input().rstrip())

    for _ in range(2):
        while s and t and s[-1] == t[-1]:
            s.pop()
            t.pop()

        s = s[::-1]
        t = t[::-1]

    if len(s) <= 1 and len(t) <= 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
