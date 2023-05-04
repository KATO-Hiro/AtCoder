# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    u = set(s)

    for si in s:
        if si in u and ("!" + si) in u:
            print(si)
            exit()

    print("satisfiable")


if __name__ == "__main__":
    main()
