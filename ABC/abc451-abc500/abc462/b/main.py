# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        _, *ai = map(int, input().split())

        for aij in ai:
            ans[aij].append(i)

    for ans_i in ans[1:]:
        size = len(ans_i)

        if size == 0:
            print(size)
        else:
            print(size, *ans_i)


if __name__ == "__main__":
    main()
