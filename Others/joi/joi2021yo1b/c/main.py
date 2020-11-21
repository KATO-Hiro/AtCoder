# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    index = a.index(max_a)

    print(sum(a[:index]))
    print(sum(a[index + 1 :]))


if __name__ == "__main__":
    main()
