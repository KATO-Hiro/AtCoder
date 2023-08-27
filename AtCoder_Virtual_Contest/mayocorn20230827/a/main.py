# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0

    for ai, bi in zip(a, b):
        if ai == bi:
            count += 1

    print(count)
    print(len(set(a) & set(b)) - count)


if __name__ == "__main__":
    main()
