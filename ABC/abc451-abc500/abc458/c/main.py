# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ans = 0

    for i, si in enumerate(s, 1):
        if si != "C":
            continue

        left = i - 1
        right = n - i
        ans += min(left, right) + 1

    print(ans)


if __name__ == "__main__":
    main()
