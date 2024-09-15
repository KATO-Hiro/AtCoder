# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(set)

    for _ in range(m):
        ai, bi = input().rstrip().split()

        if bi == "M" not in d[ai]:
            print("Yes")
        else:
            print("No")

        d[ai].add(bi)


if __name__ == "__main__":
    main()
