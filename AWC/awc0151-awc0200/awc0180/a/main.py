# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = 0

    for si in s:
        if not si.isupper():
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
