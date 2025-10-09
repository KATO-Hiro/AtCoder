# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = list()

    for ai, bi in zip(a, b):
        ans.append(ai)
        ans.append(bi)

    for ans_i in ans:
        print(ans_i)


if __name__ == "__main__":
    main()
