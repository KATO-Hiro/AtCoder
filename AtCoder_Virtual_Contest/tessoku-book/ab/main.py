# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 10**4
    ans = 0

    for _ in range(n):
        ti, ai = input().rstrip().split()
        ai = int(ai)

        if ti == "+":
            ans += ai
        elif ti == "-":
            ans -= ai
        else:
            ans *= ai

        ans %= mod
        print(ans)


if __name__ == "__main__":
    main()
