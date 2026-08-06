# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a, b = [], []

    for _ in range(n):
        si, ri = input().rstrip().split()

        if ri == "teacher" or ri == "doctor":
            a.append((si, "sensei"))

        else:
            b.append((si, "san"))

    for si, ri in a:
        print(si, ri)
    for si, ri in b:
        print(si, ri)


if __name__ == "__main__":
    main()
