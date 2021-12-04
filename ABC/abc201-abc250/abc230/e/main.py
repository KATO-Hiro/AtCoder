# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    i = 1
    ans = 0

    while i <= n:
        x = n // i
        ni = n // x + 1
        ans += x * (ni - i)
        i = ni
    
    print(ans)


if __name__ == "__main__":
    main()
