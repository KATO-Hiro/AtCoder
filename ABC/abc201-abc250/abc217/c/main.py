# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = list()

    for index, pi in enumerate(p, 1):
        q.append((pi, index))

    r = [index for qi, index in sorted(q)]
    print(*r)


if __name__ == "__main__":
    main()
