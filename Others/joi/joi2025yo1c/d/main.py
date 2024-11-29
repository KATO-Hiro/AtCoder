# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = "No"

    for i in range(1, n):
        p, q = divmod(n, i)

        if p == 1 or q != 0:
            continue

        t = s[:i]

        if t * p == s:
            ans = "Yes"
            break

    print(ans)


if __name__ == "__main__":
    main()
