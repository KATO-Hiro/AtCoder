# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    a_sum = 0

    for ai, _ in ab:
        a_sum += ai

    ans = 0

    for ai, bi in ab:
        candidate = a_sum - ai + bi
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
