# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [-1] + ([0] * n) + [-1]
    count = 0

    for ai in a:
        if 2 <= ai < n:
            if b[ai - 1] == b[ai] == b[ai + 1]:
                count += 1
            elif b[ai - 1] == b[ai + 1]:
                count -= 1
        elif ai == 1:
            if b[ai] == 0 and b[ai + 1] != 1:
                count += 1
            elif b[ai] == 1 and b[ai + 1] != 1:
                count -= 1
        elif ai == n:
            if b[ai - 1] != 1 and b[ai] == 0:
                count += 1
            elif b[ai - 1] != 1 and b[ai] == 1:
                count -= 1

        b[ai] ^= 1

        print(count)


if __name__ == "__main__":
    main()
