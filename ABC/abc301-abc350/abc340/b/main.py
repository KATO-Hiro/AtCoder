# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    values = list()

    for _ in range(q):
        i, j = map(int, input().split())

        if i == 1:
            values.append(j)
        else:
            print(values[-j])


if __name__ == "__main__":
    main()
