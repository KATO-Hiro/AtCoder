# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    candidate = -1
    ans = -1

    for i in range(n):
        ai, bi = map(int, input().split())
        ci = ai * bi

        if ci > candidate:
            candidate = ci
            ans = i + 1

    print(ans)


if __name__ == "__main__":
    main()
