# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n - 2):
        d11, d12 = d[i]
        d21, d22 = d[i + 1]
        d31, d32 = d[i + 2]

        if d11 == d12 and d21 == d22 and d31 == d32:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
