# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    m = 2 * n - 1
    ans = ["o"] * m

    for i, si in enumerate(s):
        ans[2 * i] = si

    print("".join(ans))


if __name__ == "__main__":
    main()
