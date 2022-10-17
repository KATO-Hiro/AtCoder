# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, t = map(int, input().split())
    upper = 101
    ans = 0

    for a in range(upper):
        for b in range(upper):
            for c in range(upper):
                if (a + b + c) <= s and (a * b * c <= t):
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
