# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    t = set()

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    u = set(s.copy())

    for si in s:
        if si[0] == "!":
            si = si[1:]

        t.add(si)

    for ti in t:
        if ti in u and "!" + ti in u:
            print(ti)
            exit()

    print("satisfiable")


if __name__ == "__main__":
    main()
