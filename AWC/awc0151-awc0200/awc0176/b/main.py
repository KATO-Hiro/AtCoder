# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = 0

    for i in range(n - 1):
        if s[i] == "C" and s[i + 1] == "A":
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
