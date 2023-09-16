# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ans = 1

    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            t = s[i:j]

            if t == t[::-1]:
                ans = max(ans, len(t))

    print(ans)


if __name__ == "__main__":
    main()
