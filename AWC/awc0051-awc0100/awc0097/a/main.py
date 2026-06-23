# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    l = list(map(int, input().split()))
    b = [0] * (n + 1)
    pos = 1

    for li in l:
        if b[pos] == 0:
            b[pos] = li
        elif b[pos] + li + 1 <= w:
            b[pos] += li + 1
        else:
            pos += 1
            b[pos] = li

    print(pos)


if __name__ == "__main__":
    main()
