# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    n = len(s)
    b_count = 0
    ans = 0

    for si in s[::-1]:
        count = int(si) - b_count
        count %= 10
        b_count += count
        b_count %= 10

        ans += count + 1

    print(ans)


if __name__ == "__main__":
    main()
