# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    highest = -1
    ans = []

    for ai in a:
        if ai > highest:
            highest = ai
            ans += ["o"]
        else:
            ans += ["x"]

    print("".join(ans))


if __name__ == "__main__":
    main()
