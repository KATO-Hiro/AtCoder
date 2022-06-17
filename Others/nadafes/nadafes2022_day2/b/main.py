# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = float("inf")

    for ai, bi in zip(a, b):
        ans = min(ans, ai * bi)
    
    acc_a = list(accumulate(a, func=max))
    acc_b = list(accumulate(b, func=min))

    for ai, bi in zip(acc_a, acc_b):
        ans = min(ans, ai * bi)

    print(ans)


if __name__ == "__main__":
    main()
