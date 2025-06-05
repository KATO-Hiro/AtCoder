# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n == 1:
        k = 1
        s = [1]
    else:
        k = n // 2
        s = [i for i in range(2, n + 1, 2)]

    print(k)
    print(*s)


if __name__ == "__main__":
    main()
