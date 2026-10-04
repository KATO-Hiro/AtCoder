# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    hs = []

    for i in range(n):
        hi, si, _ = map(int, input().split())
        hs.append((hi + si, i + 1))

    hs.sort(reverse=True)
    ans = hs[0][1]
    print(ans)


if __name__ == "__main__":
    main()
