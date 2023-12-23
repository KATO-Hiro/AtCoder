# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)
    ans = list()

    for ai in a:
        result = 10**9 * ai / a_max
        result *= 10
        result = int(result)

        p, q = divmod(result, 10)

        if q >= 5:
            p += 1

        ans.append(p)

    print(*ans)


if __name__ == "__main__":
    main()
