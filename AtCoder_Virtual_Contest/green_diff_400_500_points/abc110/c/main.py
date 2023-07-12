# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    ds = defaultdict(int)
    dt = defaultdict(int)

    for si, ti in zip(s, t):
        ds[si] += 1
        dt[ti] += 1

    if sorted(ds.values()) == sorted(dt.values()):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
