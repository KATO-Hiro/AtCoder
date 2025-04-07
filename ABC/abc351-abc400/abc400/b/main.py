# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = 0

    for i in range(m + 1):
        ans += n**i

        if ans > 10**9:
            ans = "inf"
            break

    print(ans)


if __name__ == "__main__":
    main()
