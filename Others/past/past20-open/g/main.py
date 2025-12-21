# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    r = sorted(list(map(int, input().split())), reverse=True)
    p = sorted(list(map(int, input().split())), reverse=True)
    odd = ceil(k, 2)
    even = k // 2
    ans = -1

    if n >= odd and m >= even:
        ans = max(ans, sum(r[:odd]) + sum(p[:even]))
    if n >= even and m >= odd:
        ans = max(ans, sum(r[:even]) + sum(p[:odd]))

    print(ans)


if __name__ == "__main__":
    main()
