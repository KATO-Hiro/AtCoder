# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, r = map(int, input().split())
    l = list(map(int, input().split()))

    ids = [i for i, li in enumerate(l) if li == 0]

    if len(ids) == 0:
        print(0)
        exit()

    left = min(ids[0], r)
    right = max(ids[-1] + 1, r)

    ans = sum(l[left:right]) + right - left
    print(ans)


if __name__ == "__main__":
    main()
