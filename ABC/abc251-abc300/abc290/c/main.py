# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = sorted(set(map(int, input().split())))
    m = min(len(a), k)
    b = set(a[:m])

    for i in range(n + 1):
        if i not in b:
            print(i)
            exit()


if __name__ == "__main__":
    main()
