# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = input().rstrip().split()
    d = {"Ocelot": 1, "Serval": 2, "Lynx": 3}

    if d[x] >= d[y]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
