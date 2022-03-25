# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    p = [[0, 0]] * n

    for i in range(n):
        pi = sum(list(map(int, input().split())))
        p[i] = [pi, i + 1]
    
    base = sorted(p, reverse=True)[k - 1][0]

    for pi, i in p:
        if pi + 300 >= base:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
