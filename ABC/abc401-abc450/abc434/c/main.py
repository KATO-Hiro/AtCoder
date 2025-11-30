# -*- coding: utf-8 -*-


def solve():
    n, h = map(int, input().split())
    prev = 0
    lower = upper = h
    ans = "Yes"
    tlu = [tuple(map(int, input().split())) for _ in range(n)]

    for now, li, ui in tlu:
        diff = now - prev
        upper = min(upper + diff, ui)
        lower = max(lower - diff, li, 1)

        if lower > upper or ui < lower or li > upper:
            ans = "No"
            break

        prev = now

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
