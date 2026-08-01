# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = "x" + input().rstrip() + "x"
    ans = 0

    for i in range(1, n + 1):
        if not (s[i - 1] == s[i] == s[i + 1] == "x"):
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
