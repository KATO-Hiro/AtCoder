# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = ""

    for i in range(1, n + 1):
        if i % 3 == 0:
            ans += "x"
        else:
            ans += "o"

    print(ans)


if __name__ == "__main__":
    main()
