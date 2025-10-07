# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = [list(input().rstrip().split(" ")) for _ in range(n)]

    for ci in c:
        if len(set(ci)) == 1:
            print("Yes")
            exit()

    for j in range(n):
        d = list()

        for i in range(n):
            d.append(c[i][j])

        if len(set(d)) == 1:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
