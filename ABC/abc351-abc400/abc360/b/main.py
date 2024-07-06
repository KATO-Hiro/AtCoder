# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, t = input().rstrip().split()
    n = len(s)

    for w in range(1, n):
        for c in range(w):
            u = ""

            for i in range(c, n, w):
                u += s[i]

            if u == t:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
