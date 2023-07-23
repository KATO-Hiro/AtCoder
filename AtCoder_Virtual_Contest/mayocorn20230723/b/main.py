# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    total = sum(t)

    for _ in range(m):
        pi, xi = map(int, input().split())
        pi -= 1

        diff = xi - t[pi]
        ans = total + diff
        print(ans)


if __name__ == "__main__":
    main()
