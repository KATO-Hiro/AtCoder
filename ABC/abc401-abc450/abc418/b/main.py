# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n + 1):

            u = s[i:j]
            m = len(u)

            if m < 3:
                continue
            if u[0] != "t" or u[-1] != "t":
                continue

            x = u.count("t")

            ratio = (x - 2) / (m - 2)
            ans = max(ans, ratio)

    print(ans)


if __name__ == "__main__":
    main()
