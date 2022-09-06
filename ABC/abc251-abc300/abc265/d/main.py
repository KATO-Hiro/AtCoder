# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    s = set([0])
    total = 0

    # See:
    # https://atcoder.jp/contests/abc265/submissions/34204256
    for ai in a:
        total += ai

        if (total - r) in s and (total - r - q) in s and (total - r - q - p) in s:
            print("Yes")
            exit()

        s.add(total)
        
    print("No")


if __name__ == "__main__":
    main()