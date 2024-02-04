# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(accumulate(a))
    b_min = min(b)

    ans = b[-1]

    if b_min < 0:
        ans += abs(b_min)

    print(ans)


if __name__ == "__main__":
    main()
