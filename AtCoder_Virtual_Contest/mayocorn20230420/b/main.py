# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    o = input().rstrip()
    e = input().rstrip()
    n, m = len(o), len(e)
    ans = [""] * (n + m)

    for i in range(n):
        ans[2 * i] = o[i]

    for i in range(m):
        ans[2 * i + 1] = e[i]

    print(''.join(ans))


if __name__ == "__main__":
    main()
