# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = set()
    y = set()

    for i in range(n):
        si = input().rstrip()

        if si[0] == "!":
            y.add(si[1:])
        else:
            x.add(si)

    result = x & y

    if len(result) == 0:
        print("satisfiable")
    else:
        print(list(result)[0])


if __name__ == "__main__":
    main()
