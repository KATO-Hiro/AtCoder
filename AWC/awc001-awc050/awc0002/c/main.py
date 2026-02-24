# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    def ceil(a: int, b: int) -> int:
        assert b != 0

        return (a + b - 1) // b

    ans = 0

    for _ in range(n):
        ai, bi = map(int, input().split())
        candidate = ceil(m - ai, bi)
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
