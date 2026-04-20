# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, m = map(int, input().split())
    f = list(map(int, input().split()))
    c = Counter(f)

    if len(set(f)) == n:
        print("Yes")
    else:
        print("No")

    ok = True

    for i in range(1, m + 1):
        if c[i] == 0:
            ok = False
            break

    if ok:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
