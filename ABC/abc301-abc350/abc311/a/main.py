# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    a, b, c = 0, 0, 0

    for i, si in enumerate(s):
        if si == "A":
            a += 1
        elif si == "B":
            b += 1
        else:
            c += 1
        # print(a, b, c)

        if a >= 1 and b >= 1 and c >= 1:
            print(i + 1)
            exit()


if __name__ == "__main__":
    main()
