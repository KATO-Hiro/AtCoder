# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    inf = 10**9
    left, right, flag = -inf, inf, 1

    for _ in range(n):
        si, pi = map(str, input().split())
        pi = int(pi)

        if si == "NEGATE":
            left, right = -right, -left
            flag *= -1
        elif si == "CHMIN":
            left = min(left, pi)
            right = min(right, pi)
        else:
            left = max(left, pi)
            right = max(right, pi)

    for _ in range(q):
        ans = int(input())
        ans *= flag
        ans = max(ans, left)
        ans = min(ans, right)
        print(ans)


if __name__ == "__main__":
    main()
