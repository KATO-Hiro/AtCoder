# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys

    input = sys.stdin.readline

    n, m, d = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 0

    for ti in t:
        candidate = ceil(ti - m, d)
        ans += max(candidate, 0)

    print(ans)


if __name__ == "__main__":
    main()
