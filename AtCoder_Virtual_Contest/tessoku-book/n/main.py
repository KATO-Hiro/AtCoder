# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    # A, BのペアとC, Dのペアを作る
    # K - (A + B) = C + Dとなるか?
    ab = defaultdict(int)
    cd = defaultdict(int)

    for ai in a:
        for bj in b:
            ab[ai + bj] += 1

    for ci in c:
        for dj in d:
            cd[ci + dj] += 1

    for ab_i in ab:
        if (k - ab_i) in cd.keys():
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
