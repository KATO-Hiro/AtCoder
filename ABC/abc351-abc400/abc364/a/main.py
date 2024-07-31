# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    for i, (si, sj) in enumerate(pairwise(s)):
        if i != n - 2 and si == sj == "sweet":
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
