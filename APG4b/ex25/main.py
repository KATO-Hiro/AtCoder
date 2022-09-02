# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline


    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    s = input().rstrip().split()
    ans = set()

    if s[0] == "intersection":
        ans = a & b
    elif s[0] == "union_set":
        ans = a | b
    elif s[0] == "symmetric_diff":
        ans = (a - b) | (b - a)
    elif s[0] == "subtract":
        x = int(s[1])
        ans = a - {x}
    elif s[0] == "increment":
        ans = {(ai + 1) % 50 for ai in a}
    elif s[0] == "decrement":
        ans = {(ai - 1) % 50 for ai in a}

    print(*sorted(ans))


if __name__ == "__main__":
    main()
