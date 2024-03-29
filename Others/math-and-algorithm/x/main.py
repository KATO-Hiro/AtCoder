# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0.0

    for i in range(n):
        pi, qi = map(int, input().split())
        ans += 1 / pi * qi

    print(ans)

if __name__ == "__main__":
    main()
