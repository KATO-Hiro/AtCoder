# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ans = set()

    for i in range(n):
        for j in range(n + 1):
            t = s[i:j]
            m = len(t)

            if m == 0:
                continue

            ans.add(t)

    print(len(ans))


if __name__ == "__main__":
    main()
