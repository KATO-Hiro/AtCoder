# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    ans = h[0]

    for i in range(1, n):
        if h[i] > h[i - 1]:
            ans = h[i]
        else:
            break

    print(ans)


if __name__ == "__main__":
    main()
