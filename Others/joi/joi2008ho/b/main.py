# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    n, m = len(s), len(t)
    right = 0
    ans = 0

    for left in range(n):
        while right < n and s[left : right + 1] in t:
            right += 1

        ans = max(ans, right - left)

    print(ans)


if __name__ == "__main__":
    main()
