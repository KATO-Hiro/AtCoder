# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse=True)

    for i in range(min(n, k)):
        h[i] = 0

    print(sum(h))


if __name__ == "__main__":
    main()
