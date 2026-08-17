# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = []

    for ai in a:
        if len(ans) == 0 or ans[-1] != ai:
            ans.append(ai)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
