# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = set(map(int, input().split()))

    for i in range(k):
        if i not in a:
            print(i)
            exit()

    print(k)


if __name__ == "__main__":
    main()
