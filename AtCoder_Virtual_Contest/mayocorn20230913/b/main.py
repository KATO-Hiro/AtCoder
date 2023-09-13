# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    tmp = list()
    ans = list()

    for i in range(1, n + 1):
        if i in a:
            tmp.append(i)
        else:
            ans.append(i)

            for ti in tmp[::-1]:
                ans.append(ti)

            tmp = []

    print(*ans)


if __name__ == "__main__":
    main()
