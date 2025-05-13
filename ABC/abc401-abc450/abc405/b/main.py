# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n + 1):
        if len(set(a)) < m:
            print(i)
            exit()

        a.pop()


if __name__ == "__main__":
    main()
