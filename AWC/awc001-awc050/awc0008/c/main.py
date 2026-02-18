# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(accumulate(a, initial=0))
    ans = 0

    for i in range(n):
        if i + k > n:
            break

        diff = b[i + k] - b[i]

        if diff <= 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
