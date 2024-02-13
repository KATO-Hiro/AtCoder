# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, d = map(int, input().split())
    ans = list()

    for i in range(a, b + 1, d):
        ans.append(i)

    print(*ans)


if __name__ == "__main__":
    main()
