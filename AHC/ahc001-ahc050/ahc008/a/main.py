# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for i in range(n):
        p = list(map(int, input().split()))

    m = int(input())

    for j in range(m):
        h = list(map(int, input().split()))

    for _ in range(300):
        print("." * m, flush=True)


if __name__ == "__main__":
    main()
