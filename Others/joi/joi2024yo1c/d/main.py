# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    ans = set()

    for p, ap in enumerate(a):
        for q, bq in enumerate(b):
            if ap + k == bq:
                ans.add((p, q))

    print(len(ans))


if __name__ == "__main__":
    main()
