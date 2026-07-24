# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    for _ in range(n):
        _, *si = map(int, input().split())
        count = 0

        for sij in si:
            if sij < k:
                continue

            count += 1

        print(count)


if __name__ == "__main__":
    main()
