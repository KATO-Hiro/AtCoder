# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n = int(input())
    qr = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())

    for _ in range(q):
        tj, dj = map(int, input().split())
        tj -= 1
        qj, rj = qr[tj]

        count = ceil((dj - rj) / qj)
        ans = qj * count + rj
        print(ans)


if __name__ == "__main__":
    main()
