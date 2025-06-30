# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    n = len(s)
    ans = "Yes"

    for i in range(1, n):
        if s[i].isupper() and s[i - 1] not in t:
            ans = "No"
            break

    print(ans)


if __name__ == "__main__":
    main()
