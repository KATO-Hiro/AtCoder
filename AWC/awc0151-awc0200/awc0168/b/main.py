# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    sum_d = sum(d)
    ans = ceil(sum_d, m)
    print(ans)


if __name__ == "__main__":
    main()
