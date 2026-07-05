# -*- coding: utf-8 -*-


def solve():
    x, y, k = map(int, input().split())
    ans = 0

    while x != y:
        if x > y:
            x //= k
        else:
            y //= k

        ans += 1

    return ans


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        ans = solve()
        print(ans)


if __name__ == "__main__":
    main()
