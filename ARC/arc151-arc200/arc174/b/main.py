# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def solve():
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    stars, counts = 0, 0

    for i, ai in enumerate(a, 1):
        stars += i * ai
        counts += ai

    needed = 3 * counts - stars
    ans = 10**18

    if needed <= 0:
        ans = 0
    else:
        ans = min(ans, needed * p[3])  # 星4のみ
        ans = min(ans, p[3] + ceil(needed - 1, 2) * p[4])  # 星4を1回 + 星5で埋める
        ans = min(ans, ceil(needed, 2) * p[4])  # 星5のみ

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
