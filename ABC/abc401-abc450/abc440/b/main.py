# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    ans = []

    for i, ti in enumerate(t, 1):
        ans.append((ti, i))

    ans.sort()

    for _, i in ans[:3]:
        print(i)


if __name__ == "__main__":
    main()
