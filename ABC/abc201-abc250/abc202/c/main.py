# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = [0 for _ in range(n)]

    for ci in c:
        d[b[ci - 1] - 1] += 1

    ans = 0

    for ai in a:
        ans += d[ai - 1]

    print(ans)


if __name__ == "__main__":
    main()
