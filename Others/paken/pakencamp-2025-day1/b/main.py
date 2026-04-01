# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)

    for _ in range(n):
        si, di = input().rstrip().split()
        d[si] = int(di)

    q = int(input())

    for _ in range(q):
        xi, yi = input().rstrip().split()
        ans = abs(d[xi] - d[yi])
        print(ans)


if __name__ == "__main__":
    main()
