# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t, p = map(int, input().split())
    l = list(map(int, input().split()))

    for day in range(102):
        count = 0

        for i in range(n):
            if l[i] >= t:
                count += 1

        if count >= p:
            print(day)
            exit()

        for i in range(n):
            l[i] += 1


if __name__ == "__main__":
    main()
