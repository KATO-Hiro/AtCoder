# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    mu = sum(a) / n

    candidates = []

    for i, ai in enumerate(a, 1):
        diff = abs(ai - mu)
        candidates.append((diff, i))

    candidates.sort(key=lambda x: (-x[0], x[1]))
    ans = candidates[0][1]
    print(ans)


if __name__ == "__main__":
    main()
