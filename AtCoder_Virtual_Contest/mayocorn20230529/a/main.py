# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            k, x = qi[1] - 1, qi[2]
            a[k] = x
        else:
            k = qi[1] - 1
            print(a[k])


if __name__ == "__main__":
    main()
