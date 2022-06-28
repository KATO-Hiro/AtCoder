# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, a, b = map(int, input().split())
    ans = 0

    while (x * a <= x + b) and (x * a < y):
        x *= a
        ans += 1
    
    ans += (y - x - 1) // b
    print(ans)


if __name__ == "__main__":
    main()
