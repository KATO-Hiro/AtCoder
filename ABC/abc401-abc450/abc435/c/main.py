# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] + list(map(int, input().split()))
    pos = 1

    for i, ai in enumerate(a):
        if i > pos:
            break

        pos = max(pos, i + ai - 1)

    pos = min(pos, n)
    print(pos)


if __name__ == "__main__":
    main()
