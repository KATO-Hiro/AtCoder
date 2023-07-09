# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    k = int(input())
    candidates = set()

    for i in range(n):
        for j in range(1, k + 1):
            if i + j > n:
                continue

            candidates.add(s[i : i + j])

    print(sorted(candidates)[k - 1])


if __name__ == "__main__":
    main()
