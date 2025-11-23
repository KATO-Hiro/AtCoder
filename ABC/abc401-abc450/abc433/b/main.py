# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        ans = -1

        for j in range(i):
            if a[j] > a[i]:
                ans = j + 1

        print(ans)


if __name__ == "__main__":
    main()
