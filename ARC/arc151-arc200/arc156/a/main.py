# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    s = input().rstrip()
    one_count = s.count("1")
    is_adjusted = s.count("11")

    if one_count % 2 == 1:
        return -1
    if one_count == 0 or one_count >= 4 or not is_adjusted:
        return one_count // 2
    if n == 3:
        return -1
    if s == "0110":
        return 3

    return 2


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        ans = solve()
        print(ans)


if __name__ == "__main__":
    main()
