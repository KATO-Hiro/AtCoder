# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] + [int(input()) for _ in range(n)]
    pos = 1
    n_max = 10 ** 5 + 10

    for i in range(n_max):
        pos = a[pos]

        if pos == 2:
            print(i + 1)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
