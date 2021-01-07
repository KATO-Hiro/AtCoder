# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = set()

    for i in range(n):
        si = input().rstrip()
        s.add(si)

    for si in s:
        if "!" + si in s:
            print(si)
            exit()

    print("satisfiable")


if __name__ == "__main__":
    main()
