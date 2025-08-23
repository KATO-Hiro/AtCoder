# -*- coding: utf-8 -*-


def solve():
    x1, x2, x3 = sorted(list(map(int, input().split())))

    x2 -= x1
    x3 -= x1
    x1 = 0

    summed = x2 + x3

    if summed % 3 == 0 and ((x1 % 2) == (x2 % 2) == (x3 % 2) == (summed % 2)):
        x2 //= 2
        x3 //= 2
        summed //= 3 * 2

        ans = summed

        if summed - x2 > 0:
            ans += summed - x2
        if summed - x3 > 0:
            ans += summed - x3

        print(ans)
    else:
        print(-1)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
