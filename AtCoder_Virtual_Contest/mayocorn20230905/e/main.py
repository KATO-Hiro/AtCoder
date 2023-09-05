# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    candidates = list()

    for ai in a:
        for bi in b:
            candidates.append(ai + bi)

    candidates = sorted(candidates, reverse=True)[: min(x * y, k)]
    # print(candidates)
    ans = list()

    for candidate in candidates:
        for ci in c:
            ans.append(candidate + ci)

    ans = sorted(ans, reverse=True)
    print(*ans[:k], sep="\n")


if __name__ == "__main__":
    main()
