# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(set(a))
    m = len(b)

    print(m)
    print(*b)


if __name__ == "__main__":
    main()
