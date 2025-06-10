# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    s = list(input().rstrip())

    # Left: 最初の s[i] > s[i + 1]
    # Right: s[i] > s[i + 1] が続く限りswap
    left = -1

    for i in range(n - 1):
        if s[i] > s[i + 1]:
            left = i
            break

    if left != -1:
        for j in range(left, n - 1):
            if s[j] < s[j + 1]:
                break

            # swap
            s[j], s[j + 1] = s[j + 1], s[j]

    print("".join(s))


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
