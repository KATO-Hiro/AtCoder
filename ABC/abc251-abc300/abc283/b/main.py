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
            ki, xi = qi[1:]
            a[ki - 1] = xi
        else:
            ki = qi[1]
            print(a[ki - 1])
    

if __name__ == "__main__":
    main()
