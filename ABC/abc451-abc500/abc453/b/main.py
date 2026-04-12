# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t, x = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**5
    prev = inf
    ans = []

    for i, ai in enumerate(a):
        if abs(prev - ai) < x:
            continue

        ans.append((i, ai))
        prev = ai

    ans.sort()

    for i, ai in ans:
        print(i, ai)


if __name__ == "__main__":
    main()
