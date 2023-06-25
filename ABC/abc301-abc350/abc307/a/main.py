# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = list()

    for i in range(n):
        ans.append(sum(a[7 * i : 7 * (i + 1)]))

    print(*ans)


if __name__ == "__main__":
    main()
