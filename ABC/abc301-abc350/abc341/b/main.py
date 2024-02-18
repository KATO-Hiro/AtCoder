# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    st = [tuple(map(int, input().split())) for _ in range(n - 1)]

    for i, (si, ti) in enumerate(st):
        bi = a[i] // si
        a[i + 1] += ti * bi

    print(a[-1])


if __name__ == "__main__":
    main()
