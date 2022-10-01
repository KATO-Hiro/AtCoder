# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = hex(n)[2:].upper()

    if len(ans) == 1:
        ans = "0" + ans

    print(ans)


if __name__ == "__main__":
    main()
