# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n + 2)
    count = 0

    for ai in a:
        if b[ai - 1] == b[ai] == b[ai + 1]:
            count += 1
        elif b[ai - 1] == b[ai + 1]:
            count -= 1

        b[ai] ^= 1

        print(count)


if __name__ == "__main__":
    main()
