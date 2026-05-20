# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0

    for bi in b:
        if bi in a:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
