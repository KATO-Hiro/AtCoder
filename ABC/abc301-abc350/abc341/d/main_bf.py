# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    candidates = [0]

    for i in range(1, 5 * 10**6 + 1):
        if i % n == 0 and i % m != 0:
            candidates.append(i)
        if i % n != 0 and i % m == 0:
            candidates.append(i)

    print(candidates[k])


if __name__ == "__main__":
    main()
