# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ok = True

    if k >= 1:
        a = sorted(a)
        b = list(accumulate(a))
    else:
        a = sorted(a, reverse=True)
        b = list(accumulate(a))

        if b[-1] < k:
            ok = False

    if ok:
        print("Yes")
        print(*a)
    else:
        print("No")


if __name__ == "__main__":
    main()
