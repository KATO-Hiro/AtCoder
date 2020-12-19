# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        if "7" not in str(i) and "7" not in str(oct(i)):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
