# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for ai in a:
        summed = c

        for aij, bi in zip(ai, b):
            summed += aij * bi

        if summed > 0:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
